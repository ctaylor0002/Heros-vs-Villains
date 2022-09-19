from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#from .serializers import SuperSerializer
from .models import Supers
#from supers import serializers


@api_view(['GET','POST'])
def supers_list(request):
    
    if request.method == 'GET':
        pass
    
