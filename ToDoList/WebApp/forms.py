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
<<<<<<< HEAD

	username = forms.CharField(required=True, max_length=30)

	password = forms.CharField(required=True, widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get('username')

		user_list = Users.objects.all()
		for user in user_list : 	
			if username == user.username:
				raise forms.ValidationError("Please choose another username")
		return username


class LoginForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['username','password']
		
	username = forms.CharField(required=True, max_length=30)

	password = forms.CharField(required=True, widget=forms.PasswordInput())

	
=======
	password = forms.CharField(widget=forms.PasswordInput())

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = Users
# 		fields = ['username','password']
>>>>>>> bd7393b23f31ffbb7de34a51705e1eb0d7abd403
