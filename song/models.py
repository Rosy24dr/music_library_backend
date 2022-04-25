from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist= models.Model(max_length=200)
    album= models.Model(max_length=200)
    release=models.DateField()
    genre=models.Model(max_length=200)
