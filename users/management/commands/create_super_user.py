from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Command to create a default superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("SUPERUSER_USERNAME")
        password = os.getenv("SUPERUSER_PASSWORD")
        email = os.getenv("SUPERUSER_EMAIL")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Successfully created'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
