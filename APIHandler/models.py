from django.db import models

# Create your models here.

class Produit(models.Model):
    id = models.IntegerField();
    nom = models.CharField(max_length=200)
    
    carac0 = models.CharField(max_length=200)
    carac1 = models.CharField(max_length=200)
    carac2 = models.CharField(max_length=200)
    carac3 = models.CharField(max_length=200)
    carac4 = models.CharField(max_length=200)
    carac5 = models.CharField(max_length=200)
    carac6 = models.CharField(max_length=200)
    carac7 = models.CharField(max_length=200)
    carac8 = models.CharField(max_length=200)
    carac9 = models.CharField(max_length=200)
    
    
    prix = models.IntegerField();