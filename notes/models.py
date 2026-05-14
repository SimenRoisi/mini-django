from django.db import models
from users.models import Organisation, User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
