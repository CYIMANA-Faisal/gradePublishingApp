from django.contrib import admin
from .models import Department, Student, Course, Enrollment, Grade


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    fields = ['name']
    list_display = ('id', 'name', 'created', 'updated')


class CourseAdmin(admin.ModelAdmin):
    model = Department
    fields = ['course_name', 'instructor', 'semester', 'enrollment_key']
    list_display = ('id', 'course_name', 'instructor', 'semester', 'enrollment_key', 'created', 'updated')


class EnrollmentAdmin(admin.ModelAdmin):
    model = Department
    fields = ['course_id', 'student_id']
    list_display = ('id', 'course_id', 'student_id',  'created', 'updated')


class GradeAdmin(admin.ModelAdmin):
    model = Department
    fields = ['course_id', 'student_id', 'mark', 'out_of', 'assessment_type', 'done_on', 'uploaded_by']
    list_display = ('id', 'course_id', 'student_id', 'mark', 'out_of', 'assessment_type', 'done_on', 'uploaded_by', 'created', 'updated')


class StudentAdmin(admin.ModelAdmin):
    model = Department
    fields = ['user_id', 'reg_no', 'level', 'department']
    list_display = ('id', 'user_id', 'reg_no', 'level', 'department', 'created', 'updated')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Student, StudentAdmin)



