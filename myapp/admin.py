from django.contrib import admin
from .models import Department, Course, Grade, School, User, Group



class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['names', 'email','reg_number', 'level', 'password','group','admin','staff','active','department']
    list_display = ('id', 'names', 'email','reg_number', 'level', 'password','group','admin','staff','active','department')

class GroupAdmin(admin.ModelAdmin):
    model = Group
    fields = ['name']
    list_display = ('id', 'name')

class SchoolAdmin(admin.ModelAdmin):
    model = School
    fields = ['name']
    list_display = ('id', 'name', 'created_at', 'updated_at')


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    fields = ['name', 'school']
    list_display = ('id', 'name', 'school', 'created_at', 'updated_at')


class CourseAdmin(admin.ModelAdmin):
    model = Course
    fields = ['code', 'level',  'academic_year', 'department', 'instructor', 'semester', 'enrollment_key']
    list_display = ('code', 'level', 'academic_year', 'department', 'instructor', 'semester', 'enrollment_key', 'created_at', 'updated_at')


class GradeAdmin(admin.ModelAdmin):
    model = Grade
    fields = ['course', 'student', 'cat', 'exam']
    list_display = ('id', 'course', 'cat', 'exam', 'created_at', 'updated_at')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)



