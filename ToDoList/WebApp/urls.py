from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='homepage'),
	url(r'^(?P<todolist_id>[0-9]+)/$', views.todo, name='todo'),
	#url(r'^(?P<question_id>[0-9]+)/savetodo/$', views.savetodo, name='savetodo'),
]