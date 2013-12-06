from django.db import models
from django.core import serializers

#-----------------------------------------------------------------------------#
# Notes : Abstract class, used to give methods for subclasses
# Status : In progress 
# Test : Untested 
class JSONModel(models.Model):

    #-----------------------------------------------------------------------------#
    # Notes : Serializing function
    # Status : 
    # Test :
    #//TODO: finish the documentation
    def to_json(self):
        return serializers.serialize('json', [self])
    
    # Used to prevent django to interprete this object as a table, aso...
    class Meta:
        abstract = True

#---------------------------------------------#
# Notes : Caracteristic Class
# Status : 
# Test :   
class Caracteristic(JSONModel):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

#-----------------------------------------------------------------------------#
# Notes : Category Class
# Status : 
# Test :
#//TODO: finish the documentation
class Category(JSONModel):
    name = models.CharField(max_length=80)
    parent_category = models.ForeignKey('self', null=True, blank=True) 
    #Null and blank are merely equal but at different level
    
#-----------------------------------------------------------------------------#
# Notes : Product Class
# Status : 
# Test :
#//TODO: finish the documentation
class Product(JSONModel):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    '''No need of n2n table, the following line is meant to create n2n table +n 
    create link between other table and n2n table'''
    caracteristics = models.ManyToManyField(Caracteristic,                  
                                            related_name='products')
    picture = models.ImageField(upload_to='pictures')
    category = models.ForeignKey(Category)
#-----------------------------------------------------------------------------#
# Notes : User class
# Status : 
# Test :
#//TODO: finish the documentation
class User(JSONModel):
    name = models.CharField(max_length=80)
    boughtProducts = models.ManyToManyField(Product,related_name='User')
