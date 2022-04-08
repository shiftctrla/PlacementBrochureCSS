from django.shortcuts import render
from .models import Student
from datetime import date

today = date.today()

def home_view(request):


    students_queryset = Student.objects.all()

    context = {
        'students':students_queryset,
        'date':today,
    }


    return render(request, 'core/index.html', context)


def profile_detail_view(request, pk):

    student_profile = Student.objects.get(pk=pk)

    context = {
        'student':student_profile
    }

    return render(request, 'core/profile_detail.html', context)




def handle404(request, exception):
    return render(request, 'core/error_templates/404.html', {})
