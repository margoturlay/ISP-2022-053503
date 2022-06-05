from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label="Ttle")
    subtitle = forms.CharField(max_length=300)
    content = forms.CharField(widget=forms.Textarea())
    post_type = forms.CharField()
    image = forms.ImageField(label="Main image")

    def clean_subtitle(self):

        subtitle = self.cleaned_data['subtitle']
        title = self.cleaned_data['title']

        if subtitle == title:
            raise ValidationError("The subtitle value should not be the same as the title")

        return subtitle