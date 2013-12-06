from django.http.response import HttpResponse
import json
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
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    jsonData = product.to_dict()    
    
    return HttpResponse(json.dumps(jsonData), mimetype='application/json')

def send_category(request, pk):
    
    try : 
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404    
    jsonData = category.to_dict()
    
    return HttpResponse(json.dumps(jsonData), mimetype='application/json')