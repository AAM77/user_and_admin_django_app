from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersManagersTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            first_name='Zulk',
            last_name='Ernan',
            email='new_user@info.com',
            password='new_user123',
            url='https://www.myportfolio.com'
            )

        self.assertEqual(user.first_name, 'Zulk')
        self.assertEqual(user.last_name, 'Ernan')
        self.assertEqual(user.email, 'new_user@info.com')
        self.assertEqual(user.password, 'new_user123')
        self.assertEqual(user.url, 'https://www.myportfolio.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)

        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='new123')
