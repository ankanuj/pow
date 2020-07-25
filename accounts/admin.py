from django.contrib import admin
from .models import User_profile,Profile_photo,Post,Comment

class User_profileAdmin(admin.ModelAdmin):
	list_display=('id','user','phone')
	list_display_links=('id','user')
	list_filter = ('user',)
	search_fields = ('user',)
	list_per_page = 25

class Profile_photoAdmin(admin.ModelAdmin):
	list_display = ('id','user','profile_photo','is_published','post_date')
	list_display_links = ('id','user','is_published')
	list_filter = ('user',)
	search_fields = ('user',)
	list_per_page = 25


class PostAdmin(admin.ModelAdmin):
	list_display = ('id','user','photo','is_published','post_date')
	list_display_links = ('id','user','is_published')
	list_filter = ('user',)
	search_fields = ('user',)
	list_per_page = 25
admin.site.register(User_profile,User_profileAdmin)
admin.site.register(Profile_photo,Profile_photoAdmin)
admin.site.register(Post,PostAdmin)



class CommentAdmin(admin.ModelAdmin):
	list_display = ('id','user','post','is_published','com_date','reply')
	list_display_links = ('id','user','is_published')
	list_filter = ('user','post')
	search_fields = ('user','post')
	list_per_page = 25


admin.site.register(Comment,CommentAdmin)

