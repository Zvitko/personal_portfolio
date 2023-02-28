from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]