from django.core.exceptions import ValidationError
from .models import Note

class NoteService:
    @staticmethod
    def create_note(*, user, validated_data):
        """
        Creates a note enforcing tenant isolation.
        """
        if not user.organisation:
            raise ValidationError("User does not belong to an organisation.")
            
        return Note.objects.create(
            author=user,
            organisation=user.organisation,
            **validated_data
        )
