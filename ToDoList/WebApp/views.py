from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.

from .models import Users, ToDoList

from .forms import ToDoForm

#def index(request):

def listoftodo(request, users_id):
	list_todo = ToDoList.objects.all()
	context = {'list_todo': list_todo}
	return render(request, 'WebApp/listoftodo.html', context)

def todo(request, todolist_id):
	todo = get_object_or_404(ToDoList, pk=todolist_id)
	data = {'title': todo.title,
			'content': todo.content,
			}
	form = ToDoForm(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		todo.title = instance.title
		todo.content = instance.content
		todo.save()
	context = {
		'todo': todo,
		'form': form
	}
	return render(request, "WebApp/todo.html", context)

#def newtodo(request, users_id):
