from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world! Welocome to my index page!')