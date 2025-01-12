from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_plantsitter = models.BooleanField(
        default=False,
        help_text="User is offering plant-sitting or other house caretaking services"
    )
    is_requester = models.BooleanField(
        default=False, 
        help_text="User is looking for plant-sitting services"
    )

    def __str__(self):
        return self.username