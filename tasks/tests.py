from django.test import TestCase, Client

# Create your tests here.
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_complete', 'due_date', 'created_at', 'updated_at', 'assigned_to']




class TaskAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
