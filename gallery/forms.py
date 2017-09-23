from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'photographer_name', 'photo_place', 'category', 'description', 'camera_used')