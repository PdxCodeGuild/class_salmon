from django.views.generic import ListView

from .models import Students

class StudentsListView(ListView):
    model = Students
    template_name = 'student_list.html'