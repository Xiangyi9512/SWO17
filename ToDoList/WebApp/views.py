from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect

from django.utils import timezone

# Create your views here.

from .models import Users, ToDoList
from .forms import ToDoForm, SignUpForm

def index(request):

	form = SignUpForm(request.POST or None)
	
	# if 'SignUp' in request.POST:

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"form" : form

	}
	return render(request,"WebApp/index.html",context)
	

	# elif 'Login' in request.POST:

	# 	if form.is_valid():
	# 		instance = form.save(commit=False)
		
	# 		user_list = Users.objects.all()
	# 		for users in user_list:
	# 			if (users.username == instance.username):
	# 				if (users.password == instance.password):
	# 					return HttpResponseRedirect(request,"WebApp/listoftodo.html")
	# 				else :
	# 					return HttpResponseRedirect(request,"WebApp/index.html")
					
	# 	return render(request,"WebApp/index.html",context)


def listoftodo(request, users_id):
	user = get_object_or_404(Users, pk=users_id)
	list_todo = user.todolist_set.all()
	context = {'list_todo': list_todo}
	return render(request, 'WebApp/listoftodo.html', context)

# def todo(request, todolist_id):
# 	todo = get_object_or_404(ToDoList, pk=todolist_id)
# 	data = {'title': todo.title,
# 			'content': todo.content,
# 			}
# 	form = ToDoForm(request.POST)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		todo.title = instance.title
# 		todo.content = instance.content
# 		todo.save()
# 	context = {
# 		'todo': todo,
# 		'form': form
# 	}
# 	return render(request, "WebApp/todo.html", context)

