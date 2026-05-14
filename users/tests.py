from django.test import TestCase
from users.models import User, Organisation

class UserManagerTests(TestCase):
    def test_create_superuser_automatically_assigns_organisation(self):
        # Act
        superuser = User.objects.create_superuser(username='super', password='password123')
        
        # Assert
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertIsNotNone(superuser.organisation)
        self.assertEqual(superuser.organisation.name, 'Admin Org')
