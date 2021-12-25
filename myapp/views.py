from django.shortcuts import render
from django.contrib.auth import authenticate, logout as django_logout, login as django_login
from django.shortcuts import render, redirect

from .models import *
# Create your views here.
def login(request):
    departments=Department.objects.all()
    groups=Group.objects.all()
    if request.method == "POST":
        user = authenticate(
            email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, '../templates/index.html',{'error':True,'message':'Invalid Credentials!','groups':groups,'departments':departments})

    else:
        return render(request, '../templates/index.html',{'error':False,'message':False,'groups':groups,'departments':departments})



def logout(request):
    django_logout(request)
    return redirect('login')



def registration(request):
    groups=Group.objects.all()
    departments=Department.objects.all()
    if request.method == "POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            return render(request, '../templates/index.html',{'error':False,'message':'User with this email already exists','groups':groups,'departments':departments})
        except User.DoesNotExist:
            # group=Group.objects.get(name=request.POST['group'])
            # department=Department.objects.get(name=request.POST['department'])
            if request.POST['reg_number']!='':
                user=User.objects.create_user(
                    names=request.POST['names'],
                    email=request.POST['email'],
                    group=request.POST['group'],
                    department=request.POST['department'],
                    password=request.POST['password']
                )
                return render(request, '../templates/index.html',{'error':False,'message':'User registered successfully! Please login','groups':groups,'departments':departments})
            
            else:
                user=User.objects.create_user(
                    names=request.POST['names'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    reg_number=request.POST['reg_number'],
                    group=request.POST['group'],
                    department=request.POST['department'],
                    level=request.POST['level']
                )
                return render(request, '../templates/index.html',{'error':False,'message':'User registered successfully! Please login','groups':groups,'departments':departments})
    else:
        
        return render(request, '../templates/index.html',{'error':False,'message':False,'groups':groups})

def update_profile(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        user.names=request.POST['names']
        user.email=request.POST['email']
        user.level=request.POST['level']
        user.save()

        return redirect('profile')

def update_password(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirm_password']:
            user=User.objects.get(id=request.user.id)
            user.set_password(request.POST['password'])
            user.save()
            django_logout(request)
            return redirect('login')
            
        else:
            return render(request,'../templates/profile.html',{'error':True})
        

    
        