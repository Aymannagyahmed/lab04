from django.db import models
from movie.models import CommonInfo
from cast.models import Cast

class Series(CommonInfo):
    casts = models.ManyToManyField(Cast,'series',through='SeriesCast')

class SeriesCast(models.Model):
    cast_id = models.ForeignKey(Cast, on_delete=models.CASCADE)    
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)



