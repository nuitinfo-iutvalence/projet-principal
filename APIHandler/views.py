from django.http.response import HttpResponse
from django.utils import simplejson



# Create your views here.
def item(request):
    some_data_to_dump = {
       'id': 'foo',
       'nom': 'bar',
       'carac0': 'carac0',
       'carac1': 'carac1',
       'carac2': 'carac2',
       'carac3': 'carac3',
       'carac4': 'carac4',
       'carac5': 'carac5',
       'carac6': 'carac6',
       'carac7': 'carac7',
       'carac8': 'carac8',
       'carac9': 'carac9',
    }
    
    data = simplejson.dumps(some_data_to_dump)
    return HttpResponse(data, mimetype='application/json')