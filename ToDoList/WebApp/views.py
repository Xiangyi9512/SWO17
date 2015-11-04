from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Users, ToDoList
from .form import SignUpForm

def index(request):

	form = SignUpForm(request.POST or None)
	
	if 'SignUp' in request.POST:

		

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
		

		context = {
			"form" : form

		}
		return render(request,"WebApp/index.html",context)


	

	elif 'Login' in request.POST:

		if form.is_valid():
			instance = form.save(commit=False)
		
			user_list = Users.objects.all()
			for users in user_list:
				if (users.username == instance.username):
					if (users.password == instance.password):
						return HttpResponseRedirect(request,"WebApp/listoftodo.html")
					else :
						return HttpResponseRedirect(request,"WebApp/index.html")
					
		return render(request,"WebApp/index.html",context)


	


def listoftodo(request):
	list_todo = ToDoList.objects.all()
	context = {'list_todo': list_todo}
	return render(request, 'WebApp/listoftodo.html', context)

def todo(request, todolist_id):
	todo = get_object_or_404(ToDoList, pk=todolist_id)
	return render(request, "WebApp/todo.html", {'todo': todo})

#def savetodo(request, todolist_id):

