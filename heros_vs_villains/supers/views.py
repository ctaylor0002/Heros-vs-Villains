from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#from heros_vs_villains.supers.serializers import SuperSerializer
from .serializers import SuperSerializer
from .models import Supers
from supers import serializers


@api_view(['GET','POST'])
def supers_list(request):
    
    if request.method == 'GET':
        
        type_param = request.query_params.get('type')

        supers = Supers.objects.all()

        if type_param:
            supers = supers.filter(super_type_id__type=type_param)



        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def supers_details(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
