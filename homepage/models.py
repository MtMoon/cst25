from django.db import models

class Birth(models.Model):
    name = models.CharField(max_length=30)
    day = models.DateField()
