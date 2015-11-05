from django import forms

from .models import Users
from .models import ToDoList

class SignUpForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['username','password']

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = Users
# 		fields = ['username','password']
	

class ToDoListForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['date','title']