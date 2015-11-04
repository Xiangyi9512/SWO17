from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Users, ToDoList

#def index(request):


def listoftodo(request):
	list_todo = ToDoList.objects.all()
	context = {'list_todo': list_todo}
	return render(request, 'WebApp/listoftodo.html', context)

def todo(request, todolist_id):
	todo = get_object_or_404(ToDoList, pk=todolist_id)
	return render(request, "WebApp/todo.html", {'todo': todo})

def savetodo(request, todolist_id):
