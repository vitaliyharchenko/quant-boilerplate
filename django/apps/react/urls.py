from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.react, name="main"),
    url(r'^task$', views.task, name="task"),
]