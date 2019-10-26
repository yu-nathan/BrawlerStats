from django.urls import path

from . import views

app_name = 'homeSite'
urlpatterns = [
    path('', views.index, name='index'),
]
