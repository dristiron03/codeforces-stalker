from django.shortcuts import render, redirect
from codeforces_crawler.forms import UserIDForm, CompareIDForm, PlagIDForm
from codeforces_crawler.forms import CompareIDFormset
from bs4 import *
from selenium import webdriver
import os
import requests
import json
import time
# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserIDForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            return render(request, 'crawler/profile.html', {'user': user})
    form = UserIDForm()
    return render(request,'crawler/login.html', {'form':form})


def profile(request):
    return render(request, 'crawler/profile.html')


def home(request):
    return render(request, 'crawler/home.html')


def compare(request):
    if request.method == 'GET':
         formset = CompareIDFormset(request.GET or None)
    elif request.method == 'POST':
        formset = CompareIDFormset(request.POST)
        if formset.is_valid():
            users = []
            for form in formset:
                user = form.cleaned_data.get('username')
                if user:
                    users.append(user)
            return render(request, 'crawler/compare.html', {'users': users})
    return render(request, 'crawler/compare_form.html', {'formset': formset})


def subFetch(contest, submission):
    print('Fetching submission ids')

    r = requests.get('https://codeforces.com/api/contest.status?contestId=' + str(contest))

    problem = None

    for sub in r.json()['result']:
        if sub['id'] == submission:
            problem = sub['problem']

    if problem == None:
        raise Exception('Submission not in this Contest.')

    submissions = []

    for sub in r.json()['result']:
        if sub['problem'] == problem and (sub['verdict'] == 'OK' or sub['id'] == submission):
            submissions.append(sub['id'])

    print('Completed Submissions Fetching')

    return submissions


def subDownload(contest, submission, submissions):
    files = []

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

    driver.get('https://codeforces.com/contest/' + str(contest) + '/submission/' + str(submission))

    code_page = driver.page_source
    soup_code = BeautifulSoup(code_page, 'lxml')
    source_text = soup_code.find("pre", id="program-source-text")

    language = source_text['class'][1][5:]

    for i in range(0, len(submissions)):

        print('\rDownloading Codes : ' + str(i + 1) + '/' + str(len(submissions)), end='')

        flag_exist = False
        lang_exist = None

        for filename in os.listdir('codes'):
            if os.path.splitext(filename)[0] == str(submissions[i]):
                flag_exist = True
                lang_exist = os.path.splitext(filename)[1][1:]

        if flag_exist:
            if lang_exist == language:
                files.append('codes/' + str(submissions[i]) + '.' + lang_exist)
            continue

        driver.get('https://codeforces.com/contest/' + str(contest) + '/submission/' + str(submissions[i]))

        code_page = driver.page_source
        soup_code = BeautifulSoup(code_page, 'lxml')
        source_text = soup_code.find("pre", id="program-source-text")

        if source_text['class'][1][5:] == language:
            files.append('codes/' + str(submissions[i]) + '.' + source_text['class'][1][5:])

        fn = open('codes/' + str(submissions[i]) + '.' + source_text['class'][1][5:], 'w')

        lines = source_text.find_all("li")

        for line in lines:
            words = line.stripped_strings
            for word in words:
                fn.write(repr(word.encode('utf-8'))[2:-1] + ' ')

            fn.write('\n')

        fn.close()

        time.sleep(2)

    driver.close()

    print('\nCompleted Downloading codes')

    return files


def mossCheck(contest,submission,files):

    urls=[]

    BLOCK_SIZE=100

    print('Starting Comparing codes')

    for file_start in range(0,len(files),BLOCK_SIZE):

        command = 'perl moss.pl -l cc codes/' + str(submission) + '.cpp '

        for file_number in range( file_start , min( len(files) , file_start + BLOCK_SIZE ) ):

            if files[file_number][6:-4] != str(submission):

                command += files[file_number] + ' '

        stream = os.popen(command)
        output = stream.read().split('\n')

        print('Comparing Codes : ' + str(file_start+1) + '/' + str(len(files)) + ' on ' + output[-2])

        try:
            lines = requests.get(output[-2]).text.split('\n')

            for i in range(len(lines)):
                if lines[i].find(str(submission))!=-1:
                    urls.append({'match': int(lines[i][-8:-6]), 'moss_url': lines[i][ lines[i].find('\"') + 1 : lines[i].find( '\"' , lines[i].find('\"') + 1 ) ], 'cf_url': 'https://codeforces.com/contest/' + str(contest) + '/submission/' + lines[i+1][ lines[i+1].find('codes/') + 6 : lines[i+1].find( '.' , lines[i+1].find('codes/') +6) ]})
        except:
            file_start -= BLOCK_SIZE

    urls = sorted(urls, key = lambda k: k['match'], reverse = True)

    return urls


def plag(request):
    if request.method == "POST":
        form = PlagIDForm(request.POST)
        if form.is_valid():
            contest = form.cleaned_data['contest']
            submission = form.cleaned_data['submission']
            submissions = subFetch(contest, submission)
            if not os.path.exists('codes'):
                os.makedirs('codes')
            files = subDownload(contest, submission, submissions)
            urls = mossCheck(contest, submission, files)
            data = {'contest': contest, 'submission': submission, 'urls': urls}
            return render(request, 'crawler/plag.html', data)
    form = PlagIDForm()
    return render(request, 'crawler/plagform.html', {'form': form})