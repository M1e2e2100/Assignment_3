from django.shortcuts import render, redirect
from .models import*

def base(request):
	context = {}
	return render(request, 'base.html', context)

def home(request):
	context = {}
	return render(request, 'home.html', context)

def about(request):
	context = {}
	return render(request, 'about.html', context)

def portfolio(request):
	project= Project.objects.all()
	context = {'Project':project}
	return render(request, 'portfolio.html', context)
