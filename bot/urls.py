
from django.conf.urls import url
from django.contrib import admin
from .views import chat

urlpatterns = [
	url(r'^chat/$', chat, name='chat'),
    url(r'^admin/', admin.site.urls)
]
