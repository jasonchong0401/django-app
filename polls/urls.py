from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello),
    #path('', views.index, name='index'),
]
