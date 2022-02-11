from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):

    def setUp(self):
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(
            email='123@admin.com',
            password='123'
        )
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email='123@client.com',
            password='123'
        )
    def test_user_listed(self):
        """test if user is correctly displayed"""
        url = reverse('admin:core_myuser_changelist')
        res = self.client.get(url)
        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)