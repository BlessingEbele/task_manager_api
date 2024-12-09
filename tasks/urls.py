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


