from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html',{'password':'32yrb2gr42ugbf'})

def password(request):
	
	characters = list('bfujrbg2ry824r')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))
	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))
	length = int(request.GET.get('length',8))
	thepassword = ''
	for x in range(length):
		thepassword += random.choice(characters)
	return render(request,'generator/password.html',{'password':thepassword})

def about(request):
	return render(request,'generator/about.html')
