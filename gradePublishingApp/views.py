from django.shortcuts import render
from myapp.models import Department
from myapp.models import Student


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    num_of_departments = Department.objects.all().count()
    num_of_students = Student.objects.all().count()
    print(num_of_departments)
    context = {
        num_of_departments: num_of_departments,
        num_of_students: num_of_students,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    return render(request, 'profile.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
