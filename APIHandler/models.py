from django.db import models

#---------------------------------------------#
# Notes : 
# Status : 
# Test :   
class Caracteristic(models.Model):
    label = models.CharField(max_length=200)

#---------------------------------------------#
# Notes : 
# Status : 
# Test :
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    caracteristics = models.ManyToManyField(Caracteristic,
                                            related_name='products')
