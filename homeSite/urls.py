from django.urls import path

from . import views

app_name = 'homeSite'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/signup', views.signup, name='signup'),
]
