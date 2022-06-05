from django.core.exceptions import TooManyFieldsSent
from django.db import models
from django.db.models.fields.related import ForeignKey

class Author(models.Model):

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, primary_key=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):

    POST_TYPES = [('c', "Commercial"), ('a', "Author")]

    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=300)
    content = models.TextField(blank=False)
    post_type = models.CharField(blank=False, max_length=1, choices=POST_TYPES)
    image = models.ImageField(upload_to="uploads")

    issued = models.DateField(blank=False)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.post_type})"