from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from app.models import Todo


class HomeView(View):

    def get(self, request):
        print("inside get")
        obj = Todo.objects.all(user=request.user)
        data = [
            {
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            }
            for todo in obj
        ]
        return HttpResponse(data)

    def post(self, request):
        data = request.POST
        todo = Todo(user=request.user, title=data['title'], description=data['description'], completed=False)
        todo.save()

        return HttpResponse(todo)
    
    def put (self, request, todo_id):
        data = request.POST
        todo = Todo.objects.get(id=todo_id)
        todo.title = data['title']
        todo.description = data['description']
        todo.completed = data['completed']
        todo.save()

        return HttpResponse(todo)

    def delete(self, request, todo_id=None):
        if todo_id is None:
            Todo.objects.all().delete()
            return HttpResponse('all deleted')
        todo = Todo.objects.get(id=todo_id)
        todo.delete()

        return HttpResponse(todo)
