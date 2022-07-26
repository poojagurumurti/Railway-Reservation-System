from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes craeted by  makemigrations

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=12, default='0000000')
    gender = models.CharField(max_length=40, default='0000000')
    medicalpractitioner = models.CharField(max_length=40, default='0000000')
    seniorcitizen = models.CharField(max_length=40, default='0000000')
    trainno = models.CharField(max_length=12, default='0000000')
    trainname = models.CharField(max_length=50, default='0000000')
    classname = models.CharField(max_length=50, default='0000000')
    noofseat = models.CharField(max_length=12, default='0000000')
    stationfrom = models.CharField(max_length=50, default='0000000')
    stationto = models.CharField(max_length=50, default='0000000')

    def str(self):
        return self.name
