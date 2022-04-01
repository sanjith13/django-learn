from django.db import models

class formcontact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
def __unicode__(self):
    return self.name
# Create your models here.for backend
