from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^get/$', views.get_data, name='get'),
]