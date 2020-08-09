# Codeforces Stalker

This was a educational project under Coding Club,IIT Guwahati.
Developed a web application that gives us a visual representation codeforces statistics/comparisons using Django and Java Script.
Used python script and Codeforces API for crawling and JS & google charts for data visualization.
A user could see his own statistics in a visual manner sorted according to the problem rating and the topics covered.
One could also see the statistics based on whether he has solved the problem in the contest or has solved it as practice.
Extended the same functionality to the compare statistics of upto 4 users at the same time.

## Requirements
```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install Django
```
## Usage 

Execute the following command from your ~/codeforces-crawler/codeforces_crawler directory in terminal.
```
python3 manage.py runserver
```

Here are some screenshots of the project:

### Homepage: Users can see a beatifully designed navigation interface when they click the hamburger.
![Screenshot from 2020-08-06 11-06-06](https://user-images.githubusercontent.com/45798981/89499443-a5f0fe00-d7dd-11ea-80bf-5d2db036e24e.png)
![Screenshot from 2020-08-06 11-05-57](https://user-images.githubusercontent.com/45798981/89499367-86f26c00-d7dd-11ea-87b3-96173badcab2.png)
![Screenshot from 2020-08-06 11-06-18](https://user-images.githubusercontent.com/45798981/89499499-c1f49f80-d7dd-11ea-809d-fe0fc188e3dd.png)

### Handle Input Page: Input Your codeforces handle in the text field 
![Screenshot from 2020-08-06 11-06-43](https://user-images.githubusercontent.com/45798981/89499751-27e12700-d7de-11ea-9fe7-46cf2a6cd9a6.png)

### User Stats Page: User can see his statistics of codeforces in the form of pie charts and conditional highlighting.
![Screenshot from 2020-08-06 11-07-04](https://user-images.githubusercontent.com/45798981/89499982-8ad2be00-d7de-11ea-8527-03fe74716a02.png)
![Screenshot from 2020-08-06 11-07-22](https://user-images.githubusercontent.com/45798981/89499991-8e664500-d7de-11ea-9741-63cabb991886.png)
![Screenshot from 2020-08-06 11-07-44](https://user-images.githubusercontent.com/45798981/89500001-90c89f00-d7de-11ea-85ea-f001b1fa4af2.png)

### Compare Form Page: User has to input upto 4 codeforces handles to compare.
![Screenshot from 2020-08-06 11-08-17](https://user-images.githubusercontent.com/45798981/89500169-e309c000-d7de-11ea-9502-487662e60d37.png)

### Compare Stats Page: User can get a visual representation of comparision between the handles inputed.
![Screenshot from 2020-08-06 11-08-53](https://user-images.githubusercontent.com/45798981/89500309-25cb9800-d7df-11ea-8078-27e3f46ec1b9.png)
![Screenshot from 2020-08-06 11-10-55](https://user-images.githubusercontent.com/45798981/89500315-28c68880-d7df-11ea-8c25-c7902fec25e3.png)

### Plag Check Page: You can give credentials of a particular submission and it will run a plag check against all submissions of the problem on codeforces and return the submissions with same/similar code after running plag check.
![Screenshot from 2020-08-09](https://github.com/dristiron03/codeforces-stalker/blob/master/img/Screenshot%20(61).png)


---

