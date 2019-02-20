from django.shortcuts import render
import datetime
# Create your views here.
from django.http import HttpResponse

def serve_time (request):
    time1= datetime.datetime.now()
#     s= "<h1> Server Time is </h1>" + str(time1)
    my_dict= {'date': time1,'name': 'Bharat','age':26,'sex': 'Male'}
    return render (request,'testapp/testapp.html',my_dict)
