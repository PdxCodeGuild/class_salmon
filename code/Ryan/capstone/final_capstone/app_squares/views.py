from django.shortcuts import render
from django.http import HttpResponse

def square(request):
    return HttpResponse("square")
