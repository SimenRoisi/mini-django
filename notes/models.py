from django.db import models
from users.models import Organisation, User

class NoteManager(models.Manager):
    def for_org(self, organisation):
        if not organisation:
            return self.none()
        return self.filter(organisation=organisation).select_related('author', 'organisation')

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = NoteManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
