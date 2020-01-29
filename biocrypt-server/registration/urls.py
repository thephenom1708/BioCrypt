from django.conf.urls import url
from . import views

app_name = 'registration'

urlpatterns = [
    url(r'^tpsend/$', views.tpsend, name='tpsend'),
    url(r'^register/$', views.register, name='register'),
    url(r'^getUserId/$', views.getUserId, name='getUserId'),
    url(r'^verifyPin/$', views.verifyPin, name='verifyPin'),
    url(r'^uploadFingerprint/$', views.uploadFingerprint, name='uploadFingerprint'),
    url(r'^getCoordinates/$', views.getCoordinates, name='getCoordinates'),
]