from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, names=None, password=None,level=None, reg_number=None,  is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have a valid email')
        if not names:
            raise ValueError('Users must have a valid names')
        if not password:
            raise ValueError("You must enter a password")

        email = self.normalize_email(email)
        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.names = names
        user_obj.level = level
        user_obj.reg_number = reg_number
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, names=None, level=None, reg_number=None, password=None):
        user = self.create_user(
            email, names=names,level=level, reg_number=reg_number, password=password, is_staff=True)
        return user

    def create_superuser(self, email, names=None, level=None, reg_number=None, password=None):
        user = self.create_user(email, names=names,level=level, reg_number=reg_number,
                                password=password, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    names = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    reg_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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

    LEVEL_ONE = 'One'
    LEVEL_TWO = 'Two'
    LEVEL_THREE = 'Three'
    LEVEL_FOUR = 'Four'

    LEVEL = (
        (LEVEL_ONE, 'One'),
        (LEVEL_TWO, 'Two'),
        (LEVEL_THREE, 'Three'),
        (LEVEL_FOUR, 'Four'),
    )

    ONE = 'One'
    TWO = 'Two'
    THREE = 'Three'
    SEMESTER = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
    )
    code = models.CharField(max_length=200)
    level = models.CharField(max_length=50, choices=LEVEL)
    academic_year = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=SEMESTER)
    enrollment_key = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


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

