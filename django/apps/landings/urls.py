from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^testing$', views.testing, name="testing"),
    url(r'^(?P<class_num>[^/]+)/(?P<subject>[^/]+)$', views.landing, name='constructor'),
]