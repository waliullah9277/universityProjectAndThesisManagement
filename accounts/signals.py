from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    User,
    UserRole,
    StudentProfile,
    SupervisorProfile,
    ExaminerProfile,
)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if not created:
        return

    if instance.role == UserRole.STUDENT:
        StudentProfile.objects.create(
            user=instance,
            student_id=f"STD{instance.id:04d}",
            department="",
            batch="",
            semester="",
        )

    elif instance.role == UserRole.SUPERVISOR:
        SupervisorProfile.objects.create(
            user=instance,
            designation="",
            department="",
        )

    elif instance.role == UserRole.EXAMINER:
        ExaminerProfile.objects.create(
            user=instance,
            designation="",
            department="",
        )