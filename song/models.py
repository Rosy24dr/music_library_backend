from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=200)
    likes = models.IntegerField(null=True)
    image_link = models.TextField(max_length=400, null=True)