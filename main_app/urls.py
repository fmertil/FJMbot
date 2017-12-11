from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[ 
    url(r'^$', views.index, name ='index'),
    url(r'^motor', views.motor, name='motor'),
   # url(r'^video', views.video, name='video'),
    url(r'^voice', views.voice, name='voice'),


]

urlpatterns +=staticfiles_urlpatterns()
