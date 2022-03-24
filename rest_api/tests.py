from asyncio.windows_events import NULL
import json
from django.urls import reverse
from rest_framework import status
from datetime import datetime
from rest_framework.test import APITestCase, URLPatternsTestCase


class TodoItemTests(APITestCase):
    def test_create_todo_item(self):
        """
        function to test todoItem creation
        """
        data = {
            'title':'test',
            'is_completed' : True,
        }
        data = json.dumps(data)
        url = reverse('create')
        response = self.client.post(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)