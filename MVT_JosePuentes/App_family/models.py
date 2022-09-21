from django.db import models

# Create your models here.

class family(models.Model):

    nombre =  models.CharField(max_length=60)
    years = models.IntegerField()
    born_in = models.DateField()
    hobbie = models.CharField(max_length=50)