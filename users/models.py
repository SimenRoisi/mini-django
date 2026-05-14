from django.db import models
from django.contrib.auth.models import AbstractUser

class Organisation(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.organisation.name if self.organisation else 'No Org'})"
