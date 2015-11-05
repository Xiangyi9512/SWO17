from django import forms
from WebApp.models import ToDoList, Users

class ToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['title', 'content']
	title = forms.CharField(required=True, max_length=100)
	content = forms.CharField(required=False, widget=forms.Textarea)

class AddNewToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['title', 'content']
	title = forms.CharField(required=True, max_length=100)
	content = forms.CharField(required=False, widget=forms.Textarea)

class DeleteToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = []

class SignUpForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['username','password']
	password = forms.CharField(widget=forms.PasswordInput())

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = Users
# 		fields = ['username','password']
