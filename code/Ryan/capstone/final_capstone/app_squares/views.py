from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("index")

# Create a new square
def CreateSquare(request):

    return render(request, "square.html")
