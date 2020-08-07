from django.urls import re_path, include
from .views import profile, login, compare, home, plag
urlpatterns = [
    re_path(r'^visualise$', profile, name='profile'),
    re_path(r'^login', login, name='login'),
    re_path(r'^compare$', compare, name='compare'),
    re_path(r'^plag$', plag, name='plag'),
    re_path(r'^$', home, name='home'),
]