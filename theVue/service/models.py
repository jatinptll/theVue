from django.db import models

# Create your models here.


class Post_content(models.Model):
    content=models.TextField()