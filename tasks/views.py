from django.shortcuts import render


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

# List and Create Tasks
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

# Retrieve, Update, and Delete Task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

# Mark Task as Complete
from rest_framework.views import APIView

class MarkTaskCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, assigned_to=request.user)
            task.is_complete = True
            task.save()
            return Response({'message': 'Task marked as complete'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views import View
# import json
# from .models import Task

# @method_decorator(csrf_exempt, name='dispatch')
# class TaskCreateView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             task = Task.objects.create(
#                 title=data['title'],
#                 description=data['description'],
#                 status=data.get('status', 'incomplete'),
#             )
#             return JsonResponse({
#                 "id": task.id,
#                 "title": task.title,
#                 "description": task.description,
#                 "status": task.status,
#                 "created_at": task.created_at
#             }, status=201)
#         except KeyError as e:
#             return JsonResponse({"error": f"Missing key: {e}"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

# class TaskListView(View):
#     def get(self, request):
#         tasks = Task.objects.all()
#         tasks_list = [
#             {
#                 "id": task.id,
#                 "title": task.title,
#                 "description": task.description,
#                 "status": task.status,
#                 "created_at": task.created_at
#             }
#             for task in tasks
#         ]
#         return JsonResponse(tasks_list, safe=False)
