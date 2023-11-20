import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User

class AccountTests(APITestCase):
    def test_create_user(self):
        valid_payload = {
             "id": 100,
             "name": "Robert100",
             "surname": "surname1",
             "email": "email@em.pl",
             "age": 2,
             "admin": True,
             "active_from": "2023-11-14T19:33:26.768000Z"
        }
        response = self.client.post(
            reverse('users.details'),
            data=json.dumps(valid_payload),
            content_type='application/json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Robert100')