from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
	
	if request.user.is_authenticated:
		return redirect('feed')
	if request.method=='POST':
		
		username = request.POST['username']
		password = request.POST['password']
	
		user = auth.authenticate(request, username=username, password=password)
		
		if user is not None:
			auth.login(request,user)
			
			return redirect('feed')
		else:
			messages.error(request,'password or username is not matched')
			return redirect('index')
		
		
	else:
		return render(request,'inventors/index.html')

def about(request):
	return render(request,'inventors/about.html')

def poems(request):
	return render(request,'inventors/poems.html')