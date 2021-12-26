from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Group(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, names=None,group=5,department=None, password=None,level=None, reg_number=None,  is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have a valid email')
        if not names:
            raise ValueError('Users must have a valid names')
        if not password:
            raise ValueError("You must enter a password")
        my_group=Group.objects.get(id=group)
        my_department=Department.objects.get(id=department)
        email = self.normalize_email(email)
        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.names = names
        user_obj.level = level
        user_obj.group = my_group
        user_obj.department = my_department
        user_obj.reg_number = reg_number
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, names=None,group=1,department=None, level=None, reg_number=None, password=None):
        user = self.create_user(
            email, names=names,group=group,department=department,level=level, reg_number=reg_number, password=password, is_staff=True)
        return user

    def create_superuser(self, email, names=None,group=1,department=None, level=None, reg_number=None, password=None):
        user = self.create_user(email, names="admin",level='0',group=group,department='department', reg_number='None',
                                password=password, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    names = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True,default="0")
    group= models.ForeignKey(Group, on_delete=models.SET_NULL,null=True,blank=True)
    department= models.ForeignKey('Department', on_delete=models.SET_NULL,null=True,blank=True)
    reg_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.names

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class School(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):

    LEVEL_ONE = '1'
    LEVEL_TWO = '2'
    LEVEL_THREE = '3'
    LEVEL_FOUR = '4'

    LEVEL = (
        (LEVEL_ONE, '1'),
        (LEVEL_TWO, '2'),
        (LEVEL_THREE, '3'),
        (LEVEL_FOUR, '4'),
    )

    ONE = '1'
    TWO = '2'
    THREE = '3'
    SEMESTER = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
    )
    code = models.CharField(max_length=200)
    level = models.CharField(max_length=50, choices=LEVEL)
    academic_year = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=SEMESTER)
    enrollment_key = models.CharField(max_length=10)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Claim(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.CharField(max_length=10000)
    payment_slip = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.FloatField(default=0.00)
    exam = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)




