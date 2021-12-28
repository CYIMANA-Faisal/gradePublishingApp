from django.db.models import Q
from django.shortcuts import render
from .decarators import allowed_users
from myapp.models import *
from django.shortcuts import render, redirect
import xlwt
from django.http import HttpResponse
import openpyxl


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    print(request.user)
    years = Year.objects.all()
    context = {
        'years': years,
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
    columns = ['Course', 'student_name', 'reg_number', 'cat marks', 'exam marks', 'total' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    grades = Marks.objects.filter(course=course_id) #dummy method to fetch data.
    for grade in grades:
        row_num = row_num + 1
        ws.write(row_num, 0, grade.course.code, font_style)
        ws.write(row_num, 1, grade.student.names, font_style)
        ws.write(row_num, 2, grade.student.reg_number, font_style)
        ws.write(row_num, 3, grade.cat, font_style)
        ws.write(row_num, 4, grade.exam, font_style)
        ws.write(row_num, 5, grade.exam+grade.cat, font_style)

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


def levels(request, dep_id):
    return render(request, 'level.html', {'department_id': dep_id})


def grades(request):
    grades=Marks.objects.filter(student=request.user.id)
    context = {
        'grades':grades
    }
    return render(request, 'grades.html', context)


def course_statistics(request,course_id):
    grades=Marks.objects.filter(course=course_id)
    context = {
        'grades':grades,
        'course_id':course_id,
    }
    return render(request, 'course_statistics.html', context)


def courses(request, year_id):
    
    courses = Course.objects.filter(lecture=request.user.id, year=year_id)
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)

def course(request, year_id):
    
    courses = Course.objects.filter(lecture=request.user.id, year=year_id)
    context = {
        'courses': courses,
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


def add_course(request):
    years = Year.objects.all()
    groups = Group.objects.filter(Q(name='lecture') | Q(name='hod'))
    leatures = User.objects.filter(group__in=groups)
    
    if request.method == 'POST':
        department = Department.objects.get(id=request.user.department.id)
        lecture= User.objects.get(id=request.POST['lecture'])
        year = Year.objects.get(id=request.POST['year'])
        course = Course()
        course.name = request.POST['name']
        course.code = request.POST['code']
        course.year = year
        course.academic_year = request.POST['academic_year']
        course.department = department
        course.lecture = lecture
        course.save()
        return render(request, 'add-course.html', {'years': years, 'leatures': leatures, 'twick':True, "message": "Course created successfully"})

    else: 
        return render(request, 'add-course.html',  {'years': years, 'leatures': leatures, 'twick':False, "message": ""})


def my_claims(request):
    claims = Claim.objects.filter(student=request.user.id)
    context = {
        'claims': claims
    }
    return render(request, 'my_claims.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
