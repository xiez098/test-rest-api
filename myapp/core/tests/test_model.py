from django.test import TestCase
from django.contrib.auth import get_user_model

class my_test_model(TestCase):
    def test_get_user(self):
        """test function for user register"""
        email="123@qq.com"
        password='123456'
        #calling default UserManager to interact with database
        user=get_user_model().objects.create_user(email=email,password=password)
        self.assertEqual(email,user.email)
        self.assertTrue(user.check_password(password))        

    def test_valide_email(self):
        """raise error if email is invalide"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'123')
    def test_create_superuser(self):
        """test creating new super user"""
        user=get_user_model().objects.create_superuser(
            'test@qq.com','123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)