from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='homepage'),
	url(r'^(?P<users_id>[0-9]+)/$', views.listoftodo, name='list'),
	url(r'^(?P<users_id>[0-9]+)/(?P<todolist_id>[0-9]+)/$', views.todo, name='todo'),	
	url(r'^(?P<users_id>[0-9]+)/(?P<todolist_id>[0-9]+)/delete/$', views.deletetodo, name='deletetodo'),
	url(r'^(?P<users_id>[0-9]+)/new/$', views.newtodo, name='newtodo'),
]