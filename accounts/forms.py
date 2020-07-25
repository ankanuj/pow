from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    image_types = ('jpg','png','jpeg')
    video_types = ('mp4','flv','avi')
    audio_types = ('mp3',)
    file_types = ('pdf','cvs','txt')
    blocked_types = ('exe','sh')
    class Meta:
        model = Post
        fields = ['status','upload_post','attachment_type']
        exclude = ['like','favorite']
        
   