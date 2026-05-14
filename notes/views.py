from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer
from .services import NoteService

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Strict tenant isolation via Manager
        user = self.request.user
        if not user.is_authenticated:
            return Note.objects.none()
        return Note.objects.for_org(user.organisation)

    def perform_create(self, serializer):
        # Delegate business logic to the Service Layer
        serializer.instance = NoteService.create_note(
            user=self.request.user,
            validated_data=serializer.validated_data
        )
