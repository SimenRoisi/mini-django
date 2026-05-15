from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Note, AuditLog

@receiver(post_save, sender=Note)
def create_audit_log(sender, instance, created, **kwargs):
    """
    Decoupled Side-Effect: Every time a Note is saved, automatically create an AuditLog entry.
    """
    if created:
        action = f"Note created by {instance.author.username}"
    else:
        action = f"Note updated by {instance.author.username}"
        
    AuditLog.objects.create(
        note=instance,
        action=action
    )
