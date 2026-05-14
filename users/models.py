from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class Organisation(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        # Automatically create or get an Admin organisation for superusers
        org, _ = Organisation.objects.get_or_create(name='Admin Org')
        extra_fields.setdefault('organisation', org)
        return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.username} ({self.organisation.name if self.organisation else 'No Org'})"
