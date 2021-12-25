from django.shortcuts import render
from myapp.models import Department, Course, School



def home(request):
    return render(request, 'index.html')


def dashboard(request):
    schools = School.objects.all()
    context = {
        'schools': schools,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    return render(request, 'profile.html')


def departments(request, school_id):
    departments = Department.objects.filter(school=school_id)
    school = School.objects.get(id=school_id)
    context = {
        'departments': departments,
        'school_name': school.name
    }
    return render(request, 'departments.html', context)


def levels(request, dep_id):
    return render(request, 'level.html', {'department_id': dep_id})


def departmentAdd(request):
    context = {
    }
    return render(request, 'add-department.html', context)


def courses(request, dep_id, level):
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
