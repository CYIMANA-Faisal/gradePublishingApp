from django.shortcuts import render
from myapp.models import Department, Student, Course



def home(request):
    return render(request, 'index.html')


def dashboard(request):
    departments = Department.objects.all()
    students = Student.objects.all()
    context = {
        'departments': len(departments),
        'students': students,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    return render(request, 'profile.html')


def department(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
    }
    return render(request, 'departments.html', context)


def departmentAdd(request):
    context = {
    }
    return render(request, 'add-department.html', context)


def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)


def addCourse(request):

    context = {
    }
    return render(request, 'add-course.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
