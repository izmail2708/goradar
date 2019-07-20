from django.shortcuts import render
from django.contrib import auth 



def front_home(request):
	return render(request, 'home/front_home.html', {'username': auth.get_user(request).username})
