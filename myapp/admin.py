from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, Course, User, Group, Marks, Student, Year
from django.forms import TextInput, Textarea



class UserAdmin(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('id','email', 'user_name', 'first_name', 'group', 'department', 'password',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        User.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'group', 'department', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

class GroupAdmin(admin.ModelAdmin):
    model = Group
    fields = ['name']
    list_display = ('id', 'name', 'created_at', 'updated_at')



class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    fields = ['name']
    list_display = ('id', 'name', 'created_at', 'updated_at')


class YearAdmin(admin.ModelAdmin):
    model = Year
    fields = ['name']
    list_display = ('id', 'name', 'created_at', 'updated_at')


class CourseAdmin(admin.ModelAdmin):
    model = Course
    fields = ['name', 'code',  'year', 'academic_year', 'department', 'lecture']
    list_display = ('name', 'code',  'year', 'academic_year', 'department', 'lecture', 'created_at', 'updated_at')


# class ClaimAdmin(admin.ModelAdmin):
#     model = Claim
#     fields = ['student', 'course', 'reason', 'is_exam', 'is_cat', 'is_reviewed', 'payment_slip']
#     list_display = ('id', 'student', 'course', 'reason', 'is_exam', 'is_cat', 'is_reviewed', 'payment_slip', 'created_at', 'updated_at')


class MarksAdmin(admin.ModelAdmin):
    model = Marks
    fields = ['course', 'student', 'cat', 'exam']
    list_display = ('id', 'course','student', 'cat', 'exam', 'created_at', 'updated_at')


class StudentAdmin(admin.ModelAdmin):
    model: Student
    fields: ['name', 'reg_number', 'department', 'year', 'password']
    list_display: ('name', 'reg_number', 'department', 'year', 'password', 'created_at', 'updated_at')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Year, YearAdmin)
# admin.site.register(Claim, ClaimAdmin)



