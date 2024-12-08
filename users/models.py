from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    profile_type = models.CharField(
        max_length=50,
        choices=[('teacher', 'Teacher'), ('student', 'Student'), ('school', 'School')]
    )

    # Add related_name to resolve reverse accessors
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change this to something unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change this to something unique
        blank=True
    )
