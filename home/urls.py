from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_home, name='front_home'),
]
