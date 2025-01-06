from django import forms
from .models import Account, Post

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['account', 'post_date', 'likes', 'dislikes', 'content_type']
