from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import User_profile,Profile_photo,Post,Comment
from django.db.models import Q
from friendship.models import Friend, Follow, Block

@login_required(login_url='index')
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')



@login_required(login_url='index')
def User_feed(request):
	u = User.objects.all().order_by('-username').exclude(username=request.user)
	following = Follow.objects.following(request.user)#list of all following
	photo = Profile_photo.objects.get(user=request.user)
	post = Post.objects.all().filter(user_id = request.user.id).order_by('-post_date')
	comment = Comment.objects.all().order_by('-id')
	
	feed=[]
	for following in following:
		pic = Post.objects.all().filter(user_id = following.id).order_by('-post_date')
		for pic in pic:
			feed.append(pic)
	content = {
			'photo': photo,
			'u':u,
			'following':following,
			'post':post,
			'feed':feed,
			'comment':comment,
		
			}
	return render(request, "accounts/User_feed.html",content)
	


def user_profile(request,pk=None):
	following = Follow.objects.following(request.user)#list of all following
	if pk:
		user = User.objects.get(pk=pk)	
	else:
		user = request.user
	pic = Post.objects.all().filter(user_id=user.id)
	all_followers = Follow.objects.followers(user)#list of all followers
	all_following = Follow.objects.following(user)#list of all following
	count_followers=0
	for followers in all_followers:
		count_followers=count_followers+1
	count_following=0
	for followers in all_following:
		count_following=count_following+1
	content = {
		'user':user,	
		'following':following,
		'pic':pic,
		'count_followers':count_followers,
		'count_following':count_following,
		'all_following':all_following,
		}

	#sending follower and followee
	if request.method == "POST":
		followee = User.objects.get(pk=pk)
		follower = request.user
		try:
			Follow.objects.add_follower(follower, followee)
		except AlreadyExistsError as e:
			ctx["errors"] = ["%s" % e]
		else:
			return redirect("profile_with_pk", pk=pk)

	return render(request, "accounts/user_profile.html", content)



@login_required(login_url='index')

def edit_profile(request):
	u = User.objects.get(username=request.user)
	user_id = u.user_profile
	edit_profile=User_profile.objects.get(user_id=u.id)
	photo = Profile_photo.objects.get(user=request.user)

	content = {
			
		'photo': photo
		}
	

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		u.first_name = first_name
		u.last_name = last_name
		u.save()
		if u.id==user_id.user_id:
			phone = request.POST['phone']
			bio = request.POST['bio']
			edit_profile.phone=phone
			edit_profile.bio=bio
			edit_profile.save()	
			return redirect('profile')	
	else:
		return render(request, "accounts/edit_profile.html",content)

@login_required(login_url='index')
def upload_image(request):
	photo = Profile_photo.objects.get(user=request.user)
	if request.method == 'POST':
		profile_photo = request.FILES['profile_photo']	
		photo.profile_photo=profile_photo
		photo.save() 
		return redirect('profile')
	else:
		return render(request, "accounts/edit_profile.html")

@login_required(login_url='index')
def upload_post(request):
	photo = Profile_photo.objects.get(user=request.user)
	u = User.objects.all().order_by('-username').exclude(username=request.user)

	content = {
		'photo': photo,
		'u':u,
		}
	if request.method == 'POST':
		user_id= request.user.id
		post = request.FILES['upload_post']
		upload = Post(photo=post,user_id = user_id)
		upload.save()
		return redirect('feed')
	else:
		return render(request,"accounts/upload_post.html",content)
	
	
@login_required(login_url='index')
def search(request):
	
	if request.method == "POST":
		search = request.POST['search']
		if search is not None:
			find = Q(username__icontains=search)
			users = User.objects.filter(find).distinct().exclude(username=request.user)
			
			
			context = {
				'users':users,
			
			}
			
		return render(request,'accounts/search.html',context)

	return render(request,'accounts/search.html')



def followers(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	pic = Post.objects.all().filter(user_id=user.id)
	all_followers = Follow.objects.followers(user)#list of all followers
	following = Follow.objects.following(request.user)#list of all following
	count_followers=0
	for followers in all_followers:
		count_followers=count_followers+1
	
	count_following=0
	for followers in following:
		count_following=count_following+1
	context = {
		'user':user,
		'followers':all_followers,
		'following':following,
		'pic':pic,
		'count_followers':count_followers,
		'count_following':count_following,

		}
	return render(request,'accounts/followers.html',context)


def following(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	pic = Post.objects.all().filter(user_id=user.id)
	all_following = Follow.objects.following(user)#list of all following
	followers = Follow.objects.followers(user)#list of all followers
	count_followers=0
	for followers in followers:
		count_followers=count_followers+1
	
	count_following=0
	for followers in all_following:
		count_following=count_following+1
	context = {
		'user':user,
		'all_following':all_following,
		'followers':followers,
		'count_followers':count_followers,
		'count_following':count_following,

		'pic':pic,


	}
	return render(request,'accounts/followers.html',context)


def unfollow(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)

	else:
		user = request.user
	content = {
		'user':user,	
		}
	""" Remove a following relationship """
	if request.method == "POST":
		followee = User.objects.get(pk=pk)
		follower = request.user
		Follow.objects.remove_follower(follower, followee)
		return redirect("profile_with_pk", pk=pk)
        

	return render(request,'accounts/user_profile.html',content)


def postdetail(request,pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.all().filter(post = post,reply=None).order_by('-id')
    user = request.user
    profile = Profile_photo.objects.get(user = request.user)
    if request.method=='POST':
        user = request.user
        post = post
        comment = request.POST['comment']
        reply_qs = None
        comments = Comment(user=user,post=post,comment=comment,reply=reply_qs)
        comments.save()
        return redirect('comment',pk=pk)
    context = {
            'comment':comment,
            'profile':profile,
            'user':user,
            'post':post,
        }
    return render(request,'accounts/comment.html',context)

def edit_post(request,pk):
	post = Post.objects.get(pk=pk)
	comment = Comment.objects.all().filter(post = post,reply=None).order_by('-id')

	if request.method == 'POST':
		user_id= request.user.id
		post = request.FILES['upload_post']
		upload = Post(pk=pk,photo=post,user_id = user_id)
		upload.save()
		return redirect('edit_post',pk=pk)
	

	context = {
		'post':post,
		'comment':comment,
		}
	return render(request,'accounts/edit_post.html',context)

def delete_post(request,pk):
	post = Post.objects.get(pk=pk)
	comment = Comment.objects.all().filter(post = post,reply=None).order_by('-id')
	context = {
			'post':post,
			'comment':comment,
			}
	if request.method=="POST":
		post.delete()
		return redirect('profile')
	else:
		return render(request,"accounts/delete_post.html",context)



def create_reply(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=='POST':
        user = request.user
        post = post
        comment = request.POST['comment']
        reply_id = request.POST['comment_id']
        reply_qs = None
        if reply_id is not None:
            reply_qs = Comment.objects.get(id=reply_id)
        comments = Comment(user=user,post=post,comment=comment,reply=reply_qs)
        comments.save()
        return redirect('comment',pk=pk)
    else:
        return render(request,'accounts/comment.html')


def report(request,pk):
	user_details = User.objects.get(pk=pk)
	context  = {
		'user_details':user_details,
	}
	return render(request,'accounts/report.html',context)