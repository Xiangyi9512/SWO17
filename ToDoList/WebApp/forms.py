from django import forms
from WebApp.models import ToDoList, Users

class ToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['title', 'content']

	# def __init__(self, *args, **kwargs):
	# 	todoinfo = kwargs.pop('todoinfo')
	# 	super(ToDoForm, self).__init__(*args, **kwargs)
	# 	self.fields['title'].initial = todoinfo

	title = forms.CharField(required=True, max_length=100)
	content = forms.CharField(required=False, widget=forms.Textarea)

class AddNewToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['title', 'content']

	# def __init__(self, *args, **kwargs):
	# 	todoinfo = kwargs.pop('todoinfo')
	# 	super(ToDoForm, self).__init__(*args, **kwargs)
	# 	self.fields['title'].initial = todoinfo

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

	
