from multiprocessing.sharedctypes import Value
from rest_framework.test import APITestCase
from core.models import User

class TestModel(APITestCase):
    """Testing user model to make sure everything is working fine"""
    def test_creates_user(self):
        user=User.objects.create_user('rizal', 'rzmobiledev@gmail.com', '441984')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'rzmobiledev@gmail.com')


    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username='', email='rzmobiledev@gmail.com', password='441984')
        self.assertRaisesMessage(ValueError,'The given username must be set')

    def test_creates_super_user(self):
        user=User.objects.create_superuser('rizal', 'rzmobiledev@gmail.com', '441984')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, 'rzmobiledev@gmail.com')