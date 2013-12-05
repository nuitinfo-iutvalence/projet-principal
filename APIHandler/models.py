from django.db import models

#---------------------------------------------#
# Notes : 
# Status : 
# Test :
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.IntegerField()

#---------------------------------------------#
# Notes : 
# Status : 
# Test :   
class Caracteristique(models.Model):
    libelle = models.CharField(max_length=200)
    
#---------------------------------------------#
# Notes : 
# Status : 
# Test :
class Possede(models.Model):
    produitID  = models.ForeignKey(Produit)
    caracteristiqueID = models.ForeignKey(Caracteristique)    
    
