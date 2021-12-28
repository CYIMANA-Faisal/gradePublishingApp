from django.shortcuts import render
from django.contrib.auth import authenticate, logout as django_logout, login as django_login
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def login(request):

    if request.method == "POST":
        user = authenticate(
            email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, '../templates/index.html',
                          {'error': True, 'message': 'Invalid Credentials! '})
    else:
        return render(request, '../templates/index.html',
                      {'error': False, 'message': False})


def logout(request):
    django_logout(request)
    return redirect('login')


def registration(request):
    groups = Group.objects.all()
    departments = Department.objects.all()
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            return render(request, '../templates/index.html',
                          {'error': False, 'message': 'User with this email already exists', 'groups': groups,
                           'departments': departments})
        except User.DoesNotExist:
            # group=Group.objects.get(name=request.POST['group'])
            # department=Department.objects.get(name=request.POST['department'])
            if request.POST['group'] == '5':
                user = User.objects.create_user(
                    names=request.POST['names'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    reg_number=request.POST['reg_number'],
                    group=request.POST['group'],
                    department=request.POST['department'],
                    level=request.POST['level'],
                    is_approved=True
                )
                return render(request, '../templates/index.html',
                              {'error': False, 'message': 'User registered successfully! Please login',
                               'groups': groups, 'departments': departments})

            else:
                user = User.objects.create_user(
                    names=request.POST['names'],
                    email=request.POST['email'],
                    group=request.POST['group'],
                    department=request.POST['department'],
                    password=request.POST['password'],
                    is_approved=False
                )
                return render(request, '../templates/index.html',
                              {'error': False, 'message': 'User registered successfully! Please login',
                               'groups': groups, 'departments': departments})
                
    else:

        return render(request, '../templates/index.html', {'error': False, 'message': False, 'groups': groups})


def update_profile(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.names = request.POST['names']
        user.email = request.POST['email']
        user.level = request.POST['level']
        user.save()

        return redirect('profile')


def update_password(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            user = User.objects.get(id=request.user.id)
            user.set_password(request.POST['password'])
            user.save()
            django_logout(request)
            return redirect('login')

        else:
            return render(request, '../templates/profile.html', {'error': True})

# def raise_claim(request):
#     grades = Grade.objects.filter(student=request.user.id)
#     course_ids = []
#     for grade in grades:
#         course_ids.append(grade.course.id)
#     courses = Course.objects.filter(id__in=course_ids)

#     if request.method == 'GET':
#         context = {
#             'courses': courses
#         }
#         return render(request, '../templates/raise-claim.html', context)
#     if request.method == 'POST':
#         cliam = {
#             'student': request.user.id,
#             'course': request.POST['course_id'],
#             'is_cat': request.POST['cat_claim'],
#             'is_cat': request.POST['exam_claim'],
#             'reason': request.POST['reason'],
#             'payment_slip': request.POST['payment_slip']
#         }
#         print(cliam)
#         context = {
#             'courses': courses,
#             'sent': ''
#         }
#         return render(request, '../templates/raise-claim.html', context)
