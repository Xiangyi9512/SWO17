from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Users, ToDoList

def listoftodo(request):
	list_todolist = ToDoList.objects.all()
	context = {'list_todolist': list_todolist}
	return render(request, 'WebApp/index.html', context)

def todo(request, todolist_id):
	question = get_object_or_404(ToDoList, pk=todolist_id)
	return render(request, "WebApp/todo.html", {'todolist': todolist})

