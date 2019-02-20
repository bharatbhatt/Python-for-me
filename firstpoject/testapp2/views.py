from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def info_view1(request):
    date1 = datetime.datetime.now()
    hrs = int(date1.strftime('%H'))
    msg = " A very good"
    if (hrs < 12 ):
        msg = msg + "Morning !!!"
    elif (hrs< 16 ):
        msg = msg + "Afternon!!!"
    else:
        msg = msg + "Night!!!"
        my_dict ={'msg':msg,'date': hrs,'name': 'Bharat','age':26,'sex': 'Male'}
    return render(request,"testapp/testapp.html",context = my_dict)
def info_view2(request):
    return HttpResponse("<h1> HI GOOD AFTERNOON INFO_VIEW2</h1>")
