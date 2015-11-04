from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listoftodo, name='listoftodo'),
	#url(r'^new/$', views.newtodo, name='newtodo'),
	url(r'^(?P<users_id>[0-9]+)/(?P<todolist_id>[0-9]+)/$', views.todo, name='todo'),
]