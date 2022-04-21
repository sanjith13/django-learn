from django.db import models

class travelform(models.Model):
    dname = models.CharField(max_length=30)
    dimg = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)
    country = models.CharField(max_length=10)
    dinfo = models.CharField(max_length=1000)
    count = models.IntegerField()

    
def __unicode__(self):
    return self.name
# Create your models here.for backend
