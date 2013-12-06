from django.db import models

#---------------------------------------------#
# Notes : Caracteristic Class
# Status : 
# Test :   
class Caracteristic(models.Model):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

#-----------------------------------------------------------------------------#
# Notes : Product Class
# Status : 
# Test :
#//TODO: finish the documentation
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    caracteristics = models.ManyToManyField(Caracteristic,
                                            related_name='products')
#-----------------------------------------------------------------------------#
# Notes : User class
# Status : 
# Test :
#//TODO: finish the documentation
class User(models.Model):
    name = models.CharField(max_length=80)
    boughtProducts = models.ManyToManyField(Product,related_name='User')
