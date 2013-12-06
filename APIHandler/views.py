from django.http.response import HttpResponse
from django.core import serializers
from django.http import Http404

from APIHandler.models import Product
from APIHandler.models import Category 

#-----------------------------------------------------------------------------#
# Notes : Function sending the json's product
# Status : 
# Test :
#//TODO: finish the documentation
def send_product(request, pk): 
    
    try : 
        product = Product.objects.get(Product, pk=pk)
    except Product.DoesNotExist:
        raise Http404
    jsonData = serializers.serialize("json", product)    
    
    return HttpResponse(jsonData, mimetype='application/json')

def send_category(request, pk):
    
    try : 
        category = Product.objects.get(Category, pk=pk)
    except Category.DoesNotExist:
        raise Http404    
    jsonData = serializers.serialize("json", category)
    
    return HttpResponse(jsonData, mimetype='application/json')