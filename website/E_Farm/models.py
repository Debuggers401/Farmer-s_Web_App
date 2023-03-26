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

    def _str_(self):
        return self.cemail

class Farmer(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    femail = models.CharField(max_length=200)
    pass1 = models.CharField(max_length=200,null=True)
    pass2 = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=15)

    def _str_(self):
        return self.femail
    
class Product(models.Model): 
    pname = models.CharField(max_length=200)
    pprice = models.IntegerField()
    pquantity = models.IntegerField()
    pimage = models.ImageField(upload_to="static/%y",default="")
 
class Cart(models.Model):
    pass

