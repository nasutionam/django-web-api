import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from .api.serializers import ProfileSerializer
from .models import Profile

class RegistrationTestCase(APITestCase):
    
    def test_registration(self):
        data = { 
            "username": "testcase",
            "email" : "testcase@localhost.net",
            "password1": "Testing100x",
            "password2": "Testing100x"
        }

        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

class ProfileViewSetTestCase(APITestCase):

    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="jhon", password="Testing100x")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    
    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.json())