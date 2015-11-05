from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='homepage'),
	url(r'^(?P<users_id>[0-9]+)/$', views.listoftodo, name='list'),
	url(r'^(?P<users_id>[0-9]+)/createnew/$', views.addnewtodo, name='addnew'),
	url(r'^(?P<users_id>[0-9]+)/(?P<todolist_id>[0-9]+)/$', views.todo, name='todo'),	
	# url(r'^(?P<todolist_id>[0-9]+)/$', views.todo, name='todo'),
]