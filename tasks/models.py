from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks_posted",
        help_text="The user who created the task"
    )
    plantsitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_taken",
        help_text="The user who accepted the task"
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title