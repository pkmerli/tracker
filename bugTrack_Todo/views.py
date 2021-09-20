from django.shortcuts import render
from Bug.models import Bug
from Todo.models import ToDo


def home_view(request):
    bug_list = Bug.objects.filter(active=True).order_by('-created_at')[:5]
    todo_list = ToDo.objects.filter(active=True).order_by('-created_at')[:5]
    return render(request, 'index.html', {'bug_list': bug_list, 'todo_list': todo_list})
