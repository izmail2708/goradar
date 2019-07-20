from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth 
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.conf import settings
from .forms import ReportForm, GreenZone, RoadNetwork, Transition, StoppingPoint, WaterBody, Yard, Buildings
from django.utils import timezone
from .decorators import check_recaptcha

def report(request):
	if request.method == "POST":
		form = ReportForm(request.POST)
		if form.is_valid():
			pot = form.save(commit=False)
			report_type = pot.report_type
			if pot.report_type == "Озеленённые территории":
				return redirect('greenzone/')	
			elif pot.report_type == "Улично-дорожная сеть":
				return redirect('roadnetwork/')
			elif pot.report_type == "Переход":
				return redirect('transition/')
			elif pot.report_type == "Остановочный пункт":
				return redirect('stoppingpoint/')
			elif pot.report_type == "Водный объект":
				return redirect('waterbody/')
			elif pot.report_type == "Двор":
				return redirect('yard/')
			elif pot.report_type == "Здание":
				return redirect('buildings/')
	else:
		form = ReportForm()
	return render(request, 'report/report.html', {'username': auth.get_user(request).username, 'form': form})

def report_greenzone(request):
	if request.method == "POST":
		form_2 = GreenZone(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Озеленённые территории"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = GreenZone()
	return render(request, 'report/report_greenzone.html', {'username': auth.get_user(request).username, 'form_2': form_2})

def report_roadnetwork(request):
	if request.method == "POST":
		form_2 = RoadNetwork(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Улично-дорожная сеть"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = RoadNetwork()
	return render(request, 'report/report_roadnetwork.html', {'username': auth.get_user(request).username, 'form_2': form_2})

def report_transition(request):
	if request.method == "POST":
		form_2 = Transition(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Переход"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = Transition()
	return render(request, 'report/report_transition.html', {'username': auth.get_user(request).username, 'form_2': form_2})

def stopping_point(request):
	if request.method == "POST":
		form_2 = StoppingPoint(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Остановочный пункт"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = StoppingPoint()
	return render(request, 'report/report_stoppingpoint.html', {'username': auth.get_user(request).username, 'form_2': form_2})

def report_waterbody(request):
	if request.method == "POST":
		form_2 = WaterBody(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Водный объект"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = WaterBody()
	return render(request, 'report/report_waterbody.html', {'username': auth.get_user(request).username, 'form_2': form_2})	

def report_yard(request):
	if request.method == "POST":
		form_2 = Yard(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Двор"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = Yard()
	return render(request, 'report/report_yard.html', {'username': auth.get_user(request).username, 'form_2': form_2})

def report_buildings(request):
	if request.method == "POST":
		form_2 = Buildings(request.POST, request.FILES)
		if form_2.is_valid():
			if request.recaptcha_is_valid:
				post = form_2.save(commit=False)
				post.report_type = "Здание"
				post.report_author = request.user
				post.report_published_date = timezone.now()
				post.save()
				return render(request, 'report/report_done.html', {'post': post, 'username': auth.get_user(request).username})
	else:
		form_2 = Buildings()
	return render(request, 'report/report_buildings.html', {'username': auth.get_user(request).username, 'form_2': form_2})	




