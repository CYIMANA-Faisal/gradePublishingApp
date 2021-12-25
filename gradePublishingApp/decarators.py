from django.http import HttpResponse
from django.shortcuts import redirect
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.group:
                group=request.user.group
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not authorized... Click on the back arrow above")
        return wrapper_func
    return decorator