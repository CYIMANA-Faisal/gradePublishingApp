from django.contrib import admin
from django.urls import path
from . import views
from myapp.views import *
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download_marks/<int:course_id>', views.download_marks, name='download_marks'),
    path('upload_marks/', views.upload_marks, name='upload_marks'),
    path('course_statistics/<int:course_id>', views.course_statistics, name='course_statistics'),
    path('grades/', views.grades, name='grades'),
    path('enroll/<int:course_id>', views.enroll, name='enroll'),
    path('update_profile/', update_profile, name='update_profile'),
    path('update_password/', update_password, name='update_password'),
    path('profile/', views.profile, name='profile'),
    path('departments/<str:school_id>/', views.departments, name='departments'),
    path('levels/<str:dep_id>/', views.levels, name='levels'),
    path('courses/<str:dep_id>/<str:level>/<str:sem_id>', views.courses, name='courses'),
    path('my_courses/', views.my_courses, name='my_courses'),
    path('courses/add', views.addCourse, name='addCourse'),
    path('my_claims/', views.my_claims, name='my_claims'),
    path('raise_claim/', raise_claim, name='raise_claim'),
    path('admin/', admin.site.urls),
]
handler404 = "gradePublishingApp.views.page_not_found_view"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )