from django.core.exceptions import ValidationError
from .models import Note
from .tasks import simulate_note_processing_task

class NoteService:
    @staticmethod
    def create_note(*, user, validated_data):
        """
        Creates a note enforcing tenant isolation.
        """
        if not user.organisation:
            raise ValidationError("User does not belong to an organisation.")
            
        note = Note.objects.create(
            author=user,
            organisation=user.organisation,
            **validated_data
        )
        
        # Trigger background task asynchronously
        simulate_note_processing_task.delay(note.id)
        
        return note
