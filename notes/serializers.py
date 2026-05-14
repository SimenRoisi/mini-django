from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    organisation_name = serializers.CharField(source='organisation.name', read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'organisation', 'organisation_name', 'author', 'author_username', 'created_at', 'updated_at']
        read_only_fields = ['organisation', 'author', 'created_at', 'updated_at']
