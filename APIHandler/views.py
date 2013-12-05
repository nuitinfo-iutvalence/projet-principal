from django.core import serializers
from django.http.response import HttpResponse
from django.utils import simplejson

from APIHandler.models import Product


def item(request):
   

    data = serializers.serialize("json", Product.objects.all())
    
    
    return HttpResponse(data, mimetype='application/json')