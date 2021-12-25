from django.contrib import admin
from django.urls import path
from . import views
from myapp.views import *
urlpatterns = [
    path('', login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('departments/<str:school_id>/', views.departments, name='departments'),
    path('levels/<str:dep_id>/', views.levels, name='levels'),
    path('departments/add', views.departmentAdd, name='addDepartment'),
    path('courses/<str:dep_id>/<str:level>', views.courses, name='courses'),
    path('courses/add', views.addCourse, name='addCourse'),
    path('admin/', admin.site.urls),
]
handler404 = "gradePublishingApp.views.page_not_found_view"
