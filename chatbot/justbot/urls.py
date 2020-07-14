from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^getdata', views.get_bot_response, name='get_bot_response'),
]