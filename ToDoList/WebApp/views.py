from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Users, ToDoList

def listoftodo(request):
	list_todolist = ToDoList.objects.all()
	context = {'list_todolist': list_todolist}
	return render(request, 'WebApp/index.html', context)

def todo(request, todolist_id):
	return HttpResponse("You're looking at todo list %s." % todolist_id)

