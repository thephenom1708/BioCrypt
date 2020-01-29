from django.conf.urls import url
from . import views

app_name = 'apitest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^returnShares/$', views.returnShares, name='returnShares'),
    url(r'^tp/$', views.tp, name='tp'),
]