from django.views.generic import ListView

from .models import Student

class StudentListView(ListView):
    model = Student 
    template_name = 'student_list.html'