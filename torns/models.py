# Create your models here.
from django.db import models

class Persona(models.Model):
    name = models.CharField(max_length=50)
    work = models.IntegerField(default=0)
    free = models.IntegerField(default=2)


class Location(models.Model):
    name = models.CharField(max_length=50)
    week = models.JSONField()

class ShiftDay(models.Model):
    day = models.DateField()


class Shift(models.Model):
    day = models.ForeignKey(ShiftDay)
    
