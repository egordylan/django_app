from rest_framework.test import APITestCase
from users.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('kate', 'katelibby@mail.com', 'password1*HkHk')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'katelibby@mail.com')

    def test_raises_error_when_no_user_name_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username='',
                          email='katelibby@mail.com',
                          password='password1*HkHk')

    def test_raises_error_with_message_when_no_user_name_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(
                username='',
                email='katelibby@mail.com',
                password='password1*HkHk')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username='kate',
                          email='',
                          password='password1*HkHk')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username='kate',
                email='',
                password='password1*HkHk')

    def test_cant_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='professor',
                email='farnsuorth@mail.com',
                password='supermegabomb',
                is_staff=False)

    def test_cant_creates_super_user_with_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='professor',
                email='farnsuorth@mail.com',
                password='supermegabomb',
                is_superuser=False)

    def test_creates_super_user(self):
        user = User.objects.create_superuser('professor', 'farnsuorth@mail.com', 'supermegabomb')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'farnsuorth@mail.com')

    # staff
    def test_cant_creates_staff_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Staffuser must have is_staff=True.'):
            User.objects.create_staffuser(
                username='staff',
                email='staff@mail.com',
                password='staffpassword123*//#R',
                is_staff=False)

    def test_cant_creates_staff_user_with_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Staffuser must have is_superuser=False.'):
            User.objects.create_staffuser(
                username='staff',
                email='staff@mail.com',
                password='staffpassword123*//#R',
                is_superuser=True)

    def test_creates_staff_user(self):
        user = User.objects.create_staffuser('staff', 'staff@mail.com', 'staffpassword123*//#R')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'staff@mail.com')
