from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_complete', 'due_date', 'created_at', 'updated_at', 'assigned_to']
