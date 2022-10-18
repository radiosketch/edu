# portfolio/urls.py

from django.conf.urls import url
from .views import *

# API Endpoints

urlpatterns = [
	url(r'^users/$', UserList.as_view()),
    url(r'^create-users/$', UserCreate.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserRetrieveUpdate.as_view()),

	url(r'^projectdisplays/$', ProjectDisplayListCreate.as_view()),
	url(r'^projectdisplays/(?P<pk>\d+)/$', ProjectDisplayRetrieveUpdate.as_view()),

	url(r'^posts/$', PostListCreate.as_view()),
	url(r'^posts/(?P<pk>\d+)/$', PostRetrieveUpdate.as_view()),
]
