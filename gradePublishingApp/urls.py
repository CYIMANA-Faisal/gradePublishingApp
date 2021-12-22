from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
handler404 = "gradePublishingApp.views.page_not_found_view"
