from django.http.response import HttpResponse
from django.utils import simplejson
from APIHandler.models import Produit 
from django.core import serializers

def item(request):
   

    data = serializers.serialize("json", Produit.objects.all())
    
    
    return HttpResponse(data, mimetype='application/json')