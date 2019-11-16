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

