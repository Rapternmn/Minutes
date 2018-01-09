from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from minutes.models import *

app_name = "minutes"

'''
1st urs ^$ means begin-end....ie localhost main page. It links to views.index function which is responsible for loading a webpage on url 127.0.0.1:8000

2nd url is responsible to load a webpage for a particular deliverable. It is a response to a click on the deliverables dropdown button on the webpage. eg 127.0.0.1:8000/4/
'''

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<member_id>[0-9]+)/$', views.detail, name='detail'),
]
