from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'students/student_list.html')
