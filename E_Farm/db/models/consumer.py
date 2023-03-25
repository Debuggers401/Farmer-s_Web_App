from django.db import models

# Create your models here.
class Consumer(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    cemail = models.CharField(max_length=200)
    pass1 = models.CharField(max_length=200,null=True)
    pass2 = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=5)
    address = models.CharField(max_length=1000)