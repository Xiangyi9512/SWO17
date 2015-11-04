from django import forms
from WebApp.models import ToDoList

class ToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['title', 'content']

	title = forms.CharField(required=True, max_length=100)
	content = forms.CharField(widget=forms.Textarea)