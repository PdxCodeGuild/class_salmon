from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world. welcome to my index page.")

def database_thing(request):
    thing_from_db = db_function()
    
