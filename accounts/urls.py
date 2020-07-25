from django.urls import path,include
from . import views

urlpatterns = [
	path('user_feed',views.User_feed,name="feed"),
	path('profile/',views.user_profile,name='profile'),
	path('other_user/{?P<pk>\d+}',views.user_profile,name='profile_with_pk'),
	path('user_edit_profile',views.edit_profile,name='edit_profile'),
	path('logout',views.logout,name='logout'),
	path('upload_image',views.upload_image,name='upload_image'),
	path('upload_post',views.upload_post,name='post'),
	path('search',views.search,name='search'),
	path('profile/followers',views.followers,name='followers_list'),
	path('other_user/followers/{?P<pk>\d+}',views.followers,name='followers_list_pk'),
	path('profile/following',views.following,name='following_list'),
	path('other_user/following/{?P<pk>\d+}',views.following,name='following_list_pk'),
	path('unfollow/{?P<pk>\d+}',views.unfollow,name='unfollow'),
	path('comment/{?P<pk>\d+}', views.postdetail,name='comment'),
    path('reply/{?P<pk>\d+}', views.create_reply,name='reply'),
    path('edit/post/{?P<pk>\d+}', views.edit_post,name='edit_post'),
    path('delete/post/{?P<pk>\d+}', views.delete_post,name='delete_post'),
	path('report/user/{?p<pk>\d+}',views.report,name="report")





]