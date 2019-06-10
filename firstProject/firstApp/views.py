from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad_vacancy (request):
    s= '<h1> Hi welecome to our hyderabad page</h1><hr>'
    s=s+'Numbers of opening are 100'
    return HttpResponse(s)

#bangalore view here
def bangalore_vacancy(request):
    s='<h1> Hi welecome to our Bangalore page</h1><hr>'
    s=s+'Numbers of opening are 100'
    return HttpResponse(s)
