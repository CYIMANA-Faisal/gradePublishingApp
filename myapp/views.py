from django.shortcuts import render
from django.contrib.auth import authenticate, logout as django_logout, login as django_login
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == "POST":
        user = authenticate(
            email=request.POST['email'], password=request.POST['password'])
        django_login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'templates/index.html')