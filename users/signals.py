from django.db.models.signals import post_migrate, post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from tasks.models import Task
from .models import User

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    requester_group, created = Group.objects.get_or_create(name="Requester")
    if created:
        task_content_type = ContentType.objects.get_for_model(Task)
        requester_group.permissions.add(
            Permission.objects.get(codename="add_task", content_type=task_content_type),
            Permission.objects.get(codename="view_task", content_type=task_content_type),
            Permission.objects.get(codename="delete_task", content_type=task_content_type),
        )

    plantsitter_group, created = Group.objects.get_or_create(name="Plantsitter")
    if created:
        task_content_type = ContentType.objects.get_for_model(Task)
        plantsitter_group.permissions.add(
            Permission.objects.get(codename="view_task", content_type=task_content_type),
        )

@receiver(post_save, sender=User)
def assign_user_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_plantsitter:
            group, _ = Group.objects.get_or_create(name="Plantsitter")
            instance.groups.add(group)
        if instance.is_requester:
            group, _ = Group.objects.get_or_create(name="Requester")
            instance.groups.add(group)