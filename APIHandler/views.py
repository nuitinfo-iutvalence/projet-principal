from django.http import Http404
from django.http.response import HttpResponse
import json

from APIHandler.models import Caracteristic, Category, Product


#-----------------------------------------------------------------------------#
# Notes : Function sending the json's product
# Status : 
# Test :
# //TODO: finish the documentation
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
    return HttpResponse(jsonData, mimetype='application/json')

def answer_search(request):
    q = request.GET['q'].lower()
    keywords = q.split()
    
    qs = Product.objects.all()
    for kw in keywords:
        qs = qs.filter(name__contains=kw)
        
    data = [p.to_dict() for p in qs]
        
    return HttpResponse(json.dumps(data), mimetype='application/json')

