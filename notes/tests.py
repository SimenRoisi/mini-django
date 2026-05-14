from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User, Organisation
from .models import Note

class TenantIsolationTests(TestCase):
    def setUp(self):
        # Create Org 1 and User 1
        self.org1 = Organisation.objects.create(name='Org 1')
        self.user1 = User.objects.create_user(username='user1', password='password123', organisation=self.org1)
        
        # Create Org 2 and User 2
        self.org2 = Organisation.objects.create(name='Org 2')
        self.user2 = User.objects.create_user(username='user2', password='password123', organisation=self.org2)
        
        # Create Notes
        self.note1 = Note.objects.create(title='Note 1', content='Org 1 Note', organisation=self.org1, author=self.user1)
        self.note2 = Note.objects.create(title='Note 2', content='Org 2 Note', organisation=self.org2, author=self.user2)
        
        self.client = APIClient()

    def test_user_can_only_see_their_orgs_notes(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get('/api/notes/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Note 1')

    def test_user_creates_note_in_their_org(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.post('/api/notes/', {'title': 'New Note', 'content': 'Test Content'})
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['organisation'], self.org2.id)
        self.assertEqual(response.data['author'], self.user2.id)
        
        # Verify in DB
        note = Note.objects.get(id=response.data['id'])
        self.assertEqual(note.organisation, self.org2)
