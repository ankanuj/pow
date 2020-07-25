from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class User_profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phone = models.CharField(blank=True,max_length=13)
    bio = models.CharField(max_length=300,blank=True)
    
    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User_profile.objects.create(user=instance)

    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user_profile.save()

class Profile_photo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_photo = models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published=models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_profile_photo(sender, instance, created, **kwargs):
        if created:
            Profile_photo.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_profile_photo(sender, instance, **kwargs):
        instance.profile_photo.save()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    photo = models.ImageField(upload_to='users/post/%y/%m/%d/',blank=True,null=True,max_length=50)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    com_date = models.DateTimeField(default=datetime.now,blank=True)
    is_published=models.BooleanField(default=True)
    reply = models.ForeignKey('self',null=True,related_name='replies',blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment