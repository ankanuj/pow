from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']

		conf_password = request.POST['conf_password']

		
		if password == conf_password:
			#check user name
			if User.objects.filter(username=username).exists():
				messages.error(request,'That username is taken')
				return redirect('signup')
			else:
				user = User.objects.create_user(username=username,first_name = first_name, last_name = last_name, email = email, password=password)
				user.save()
				messages.success(request,'Successfully registered now login')
				return redirect('index')

		else:
			messages.error(request,'Password not matched')
			return redirect('signup')
		
	else:
		return render(request,'registration/signup.html')

		





