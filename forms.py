from django import forms
from blogam.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"