from django.shortcuts import render
from myapp.models import Department, Course, Grade, School
from .decarators import allowed_users
from myapp.models import *
from django.shortcuts import render, redirect
import xlwt
from django.http import HttpResponse
import openpyxl


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    schools = School.objects.all()
    context = {
        'schools': schools,
    }
    return render(request, 'dashboard.html', context)

def upload_marks(request):
    pass


def profile(request):
    return render(request, 'profile.html')

def download_marks(request,course_id):
    response=HttpResponse(content_type='application/ms-excel')
    course=Course.objects.get(id=course_id)
    #decide file name
    response['Content-Disposition'] = f'attachment; filename="{course.code}-marks.xls"'

    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    #column header names, you can use your own headers here
    columns = [ 'ID','Course', 'student', 'reg_number', 'cat marks', 'exam marks', 'total' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    grades = Grade.objects.filter(course=course_id) #dummy method to fetch data.
    for grade in grades:
        row_num = row_num + 1
        ws.write(row_num, 0, grade.id, font_style)
        ws.write(row_num, 1, grade.course.code, font_style)
        ws.write(row_num, 2, grade.student.names, font_style)
        ws.write(row_num, 3, grade.student.reg_number, font_style)
        ws.write(row_num, 4, grade.cat, font_style)
        ws.write(row_num, 5, grade.exam, font_style)
        ws.write(row_num, 6, grade.exam+grade.cat, font_style)

    wb.save(response)
    return response


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

def grades(request):
    grades=Grade.objects.filter(student=request.user.id)
    context = {
        'grades':grades
    }
    return render(request, 'grades.html', context)


def course_statistics(request,course_id):
    grades=Grade.objects.filter(course=course_id)
    context = {
        'grades':grades,
        'course_id':course_id,
    }
    return render(request, 'course_statistics.html', context)


def courses(request, dep_id, level, sem_id):
    courses = Course.objects.filter(department=dep_id,level=level,semester=sem_id)
    grades = Grade.objects.all()
    grade_ids=[]
    for grade in grades:
        grade_ids.append(grade.student.id)
    context = {
        'courses': courses,
        'grade_ids': grade_ids,
        'dep_id': dep_id,
        'level': level,
        'sem_id': sem_id,
    }
    return render(request, 'courses.html', context)


def my_courses(request):
    grades = Grade.objects.filter(student=request.user.id)
    course_ids=[]
    for grade in grades:
        course_ids.append(grade.course.id)
    courses= Course.objects.filter(id__in=course_ids)
    context = {
        'courses': courses,
    }
    return render(request, 'my_courses.html', context)

def enroll(request,course_id):
    if request.method=='POST':
        course=Course.objects.get(id=course_id)
        if request.POST['enrollment_key']==course.enrollment_key:
            grade=Grade()
            user=User.objects.get(id=request.user.id)
            grade.course=course
            grade.student=user
            grade.save()
            
            context = {
            'course_id': course_id,
            'error': False,
            }
            return render(request, 'enroll.html', context)
            
        else:
            context = {
            'course_id': course_id,
            'error': True,
            }
            return render(request, 'enroll.html', context)
    else:
        context = {
            'course_id': course_id,
            'error': False,
        }
        return render(request, 'enroll.html', context)


def addCourse(request):

    context = {
    }
    return render(request, 'add-course.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
