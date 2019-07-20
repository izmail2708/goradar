from django.urls import path
from . import views
from .decorators import check_recaptcha

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', check_recaptcha(views.register), name='register'),
]
