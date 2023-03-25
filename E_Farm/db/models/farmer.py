from django.db import models

# Create your models here.
class Farmer(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    femail = models.CharField(max_length=200)
    pass1 = models.CharField(max_length=200,null=True)
    pass2 = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=15)

    @staticmethod
    def getFarmerByEmail(email):
        return Farmer.objects.filter(cemail=email)