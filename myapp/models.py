from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Group(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    reg_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, blank=True)
    password = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CustomAccountManager(BaseUserManager):

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def create_superuser(self, email, user_name, first_name, group, department, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, group, department, password, **other_fields)

    def create_user(self, email, user_name, first_name, group, department, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        group = Group.objects.get(id=group)
        department = Department.objects.get(id=department)

        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, group=group, department=department,  **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'group', 'department']

    def __str__(self):
        return self.user_name
# class UserManager(BaseUserManager):
#     def create_user(
#             self,
#             email,
#             names,
#             group,
#             department=None,
#             password=None,
#             **other_fields
#     ):
#         if not email:
#             raise ValueError('Users must have a valid email')
#         if not names:
#             raise ValueError('Users must have a valid names')
#         if not password:
#             raise ValueError("You must enter a password")

#         group = Group.objects.get(id=group)
#         if not is_admin:
#             department = Department.objects.filter(id=department)
#         else:
#             department = ''
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             names=names,
#             group=group,
#             department=department
#         )
#         user.set_password(password)
#         user.save()
#         return user

#     def create_staffuser(
#             self,
#             email,
#             names=None,
#             group=None,
#             department=None,
#             password=None,
#             is_active=True,
#             is_staff=True,
#             is_admin=False
#     ):
#         user = self.create_user(
#             email,
#             names=names,
#             group=group,
#             department=department,
#             password=password,
#             is_active=is_active,
#             is_staff=is_staff,
#             is_admin=is_admin
#         )
#         return user

#     def create_superuser(
#             self,
#             email,
#             names,
#             group,
#             department,
#             password,
#             **other_fields
#     ):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError("Superuser must be assigned is_staff=True")

#         if other_fields.get('is_superuser') is not True:
#             raise ValueError("Superuser must be assigned is_superuser=True")

#         return self.create_user(self, email, names, group, department, password, **other_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     names = models.CharField(max_length=255, null=True, blank=True)
#     group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
#     department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['names', 'group', 'department']

#     def __str__(self):
#         return self.names

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, blank=True)
    academic_year = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    lecture = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Claim(models.Model):
#     student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
#     reason = models.CharField(max_length=10000)
#     is_exam = models.BooleanField(default=False)
#     is_cat = models.BooleanField(default=False)
#     payment_slip = models.ImageField(null=True, blank=True)
#     is_reviewed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     field_values = []
    #     for field in self._meta.get_fields():
    #         field_values.append(str(getattr(self, field.name, '')))
    #     return ' '.join(field_values)


class Marks(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cat = models.FloatField(default=0, blank=True)
    exam = models.FloatField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
