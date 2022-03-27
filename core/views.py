from django.shortcuts import render
from .models import Student

def home_view(request):

    students_queryset = Student.objects.all()

    context = {
        'students':students_queryset,
    }


    return render(request, 'core/index.html', context)
