from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from accounts.validators import validate_phone

from .managers import UserManager


# user role choices
class UserRole(models.TextChoices):
    
    ADMIN = "ADMIN", "Admin"

    STUDENT = "STUDENT", "Student"

    SUPERVISOR = "SUPERVISOR", "Supervisor"

    EXAMINER = "EXAMINER", "Examiner"


# user model
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20, blank=True)

    role = models.CharField(
    max_length=20,
    choices=UserRole.choices,
    default=UserRole.STUDENT
)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    phone = models.CharField(
    max_length=20,
    validators=[validate_phone],
    blank=True
    )


    def __str__(self):
        return self.email
    class Meta:
        ordering = ["id"]

# student profile models
class StudentProfile(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(max_length=30, unique=True)

    # department = models.CharField(max_length=100)
    department = models.CharField(
    max_length=100,
    blank=True,
    )
    batch = models.CharField(
    max_length=20,
    blank=True,
    )

    semester = models.CharField(
        max_length=20,
        blank=True,
    )

    # batch = models.CharField(max_length=20)

    # semester = models.CharField(max_length=20)

    cgpa = models.DecimalField(
    max_digits=4,
    decimal_places=2,
    default=0
    )

    session = models.CharField(
        max_length=30,
        blank=True
    )

    def __str__(self):
        return self.student_id

# supervisor profile models
class SupervisorProfile(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="supervisor_profile"
    )

    # designation = models.CharField(max_length=100)

    # department = models.CharField(max_length=100)
    designation = models.CharField(
    max_length=100,
    blank=True,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
    )

    faculty_id = models.CharField(
    max_length=30,
    blank=True
    )

    office_room = models.CharField(
        max_length=30,
        blank=True
    )

    def __str__(self):
        return self.user.email
    
# examiner profile models
class ExaminerProfile(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="examiner_profile"
    )

    # designation = models.CharField(max_length=100)

    # department = models.CharField(max_length=100)
    designation = models.CharField(
    max_length=100,
    blank=True,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
    )

    faculty_id = models.CharField(
    max_length=30,
    blank=True
    )

    office_room = models.CharField(
        max_length=30,
        blank=True
    )

    def __str__(self):
        return self.user.email
    

avatar = models.ImageField(
    upload_to="users/avatar/",
    blank=True,
    null=True
)

date_of_birth = models.DateField(
    blank=True,
    null=True
)

gender = models.CharField(
    max_length=10,
    blank=True
)

class Meta:
    ordering = ["id"]
    verbose_name = "User"
    verbose_name_plural = "Users"