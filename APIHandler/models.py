from django.db import models

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
    def to_dict(self):
        raise {}
    
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
    
    def to_dict(self):
        return {'nom' : self.label,
                'valeur' : self.valeur
                }
    
#-----------------------------------------------------------------------------#
# Notes : Category Class
# Status : 
# Test :
#//TODO: finish the documentation
class Category(JSONModel):
    name = models.CharField(max_length=80)
    parent_category = models.ForeignKey('self', null=True, blank=True) 
    #Null and blank are merely equal but at different level
    
    def to_dict(self):
        return {'nom':self.name,
                'categorie_parent':self.parent_category
                }
    
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
    # Notes : 
    # Status : 
    # Test :
    #//TODO: finish the documentation
    def to_dict(self):
        return {'pk': self.pk,
               'picture': self.picture.url,
               'category': self.category.to_dict(),
               'price': self.price,
               'name': self.name,
               'caracteristics': [c.to_dict() for c in self.caracteristics.all()], 
               #TODO: re check, so huge !
               }
#-----------------------------------------------------------------------------#
# Notes : User class
# Status : 
# Test :
#//TODO: finish the documentation
class User(JSONModel):
    name = models.CharField(max_length=80)
    boughtProducts = models.ManyToManyField(Product,related_name='User')
    
    def to_dict(self):
        return {'nom':self.name,
                'produits_achetes':[p.to_dict() for p in self.boughtProducts.all()]
                }