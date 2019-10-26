from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import User_profile


@login_required(login_url='index')
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')

@login_required(login_url='index')

def User_feed(request):
	return render(request,"accounts/User_feed.html")



@login_required(login_url='index')

def user_profile(request):
	profile = User_profile.objects.all()
	content = {
		'profile' : profile
	}
	return render(request,"accounts/user_profile.html",content)



@login_required(login_url='inventors/index')

def edit_profile(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		phone = request.POST['phone']
		bio = request.POST['bio']
		edit_profile = User_profile(first_name = first_name,last_name = last_name, email = email, phone = phone, bio = bio)
		edit_profile.save()
		return redirect('User_profile')


	else:
		return render(request, "accounts/edit_profile.html")
