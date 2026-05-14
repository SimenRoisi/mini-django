from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        # Strict tenant isolation: Only return notes for the user's organisation
        user = self.request.user
        if not user.is_authenticated or not user.organisation:
            return Note.objects.none()
        return Note.objects.filter(organisation=user.organisation)

    def perform_create(self, serializer):
        # Automatically assign the author and the user's organisation to the new Note
        serializer.save(
            author=self.request.user,
            organisation=self.request.user.organisation
        )
