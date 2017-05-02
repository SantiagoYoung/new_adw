




from django.http import HttpResponse
import json

def Json_Response(*args):

    data = json.dumps(*args)

    return HttpResponse(data, content_type='application/json')








