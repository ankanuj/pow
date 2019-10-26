from django.urls import path
from . import views

urlpatterns = [
	path('user_feed/',views.User_feed,name="feed"),
	path('user_profile/',views.user_profile,name='profile'),
	path('user_edit_profile',views.edit_profile,name='edit_profile'),
	path('logout',views.logout,name='logout'),

	

]