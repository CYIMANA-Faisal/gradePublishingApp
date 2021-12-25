from django.shortcuts import render
from myapp.models import Department, Course, Grade, School
from .decarators import allowed_users


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


# def courses(request):
#     courses = Course.objects.filter(=school_id)
#     school = School.objects.get(id=school_id)
#     context = {
#         'departments': departments,
#         'school_name': school.name
#     }
#     return render(request, 'departments.html', context)


def levels(request, dep_id):
    return render(request, 'level.html', {'department_id': dep_id})

# def semesters(request):
#     return render(request, 'level.html', {'department_id': dep_id})

def departmentAdd(request):
    context = {
    }
    return render(request, 'add-department.html', context)


def courses(request, dep_id, level, sem_id):
    courses = Course.objects.filter(department=dep_id,level=level,semester=sem_id)
    grades = Grade.objects.all()
    grade_ids=[]
    for grade in grades:
        grade_ids.append(grade.student.id)
    context = {
        'courses': courses,
        'grade_ids': grade_ids,
        'dep_id':dep_id,
        'level':level,
        'sem_id':sem_id,
    }
    return render(request, 'courses.html', context)


def addCourse(request):

    context = {
    }
    return render(request, 'add-course.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
