from django.shortcuts import render



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Task

@method_decorator(csrf_exempt, name='dispatch')
class TaskCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                title=data['title'],
                description=data['description'],
                status=data.get('status', 'incomplete'),
            )
            return JsonResponse({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "created_at": task.created_at
            }, status=201)
        except KeyError as e:
            return JsonResponse({"error": f"Missing key: {e}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        tasks_list = [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "created_at": task.created_at
            }
            for task in tasks
        ]
        return JsonResponse(tasks_list, safe=False)
