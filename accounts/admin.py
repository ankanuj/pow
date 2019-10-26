from django.contrib import admin
from .models import User_profile

class User_profileAdmin(admin.ModelAdmin):
	list_display=('id','user','first_name','last_name','email','phone')
	list_display_links=('id','user')
	list_filter = ('user',)
	search_fields = ('user','email')
	list_per_page = 25

admin.site.register(User_profile,User_profileAdmin)
