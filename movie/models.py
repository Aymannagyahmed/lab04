from typing import AbstractSet
from django.db import models
from cast.models import Cast
from category.models import Category

class CommonInfo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField()
    poster_image = models.ImageField(upload_to='movie_poster')
    

    class Meta:
        abstract = True

class Movie(CommonInfo):
    casts = models.ManyToManyField(Cast,'movies')
    categories = models.ManyToManyField(Category,'movies')
    def __str__(self):
        return self.title






