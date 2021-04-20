from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HtppResponse("Hi! WWelcome to my Django Application on Zuri")
