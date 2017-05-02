from django.shortcuts import render

from rest_framework import viewsets
from serializers import SystemInformationSerializer

from .models import *
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt






@csrf_exempt
def suggestion(request):

    if request.method == 'POST':

        content = request.POST.get('content', None)

        if not content:
            return JsonResponse({'status': 0, 'message': 'error'})

        Suggesstion.objects.create(content=content)

        return JsonResponse({"status": 1, 'message': 'success'})

    return JsonResponse({'status': 0})




class SystemInformationViewSet(viewsets.ModelViewSet):

    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializer











