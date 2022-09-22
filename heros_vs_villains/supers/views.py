from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#from heros_vs_villains.supers.serializers import SuperSerializer
from .serializers import SuperSerializer
from .models import Supers
from supers import serializers
from super_types.models import SuperType


@api_view(['GET','POST'])
def supers_list(request):
    
    if request.method == 'GET':
        
        type_param = request.query_params.get('type')

        supers = Supers.objects.all()

        if type_param:
            supers = supers.filter(super_type_id__type=type_param)



        super_types = SuperType.objects.all()

        custom_response_dictionary = {}

        for super_type in super_types:

            supers = Supers.objects.filter(super_type_id = super_type.id)
            
            super_serializer = SuperSerializer(supers, many=True)

            custom_response_dictionary[super_type.type] = {
                super_type.type : super_serializer.data,
            }



        # super_serializer = SuperSerializer(supers, many=True)

        # return Response(serializer.data)

        # super_types = SuperType.objects.all()

        # custom_response_dictionary = {}
    
        # for super in supers:
        #    supers = Supers.objects.filter(super_type_id = super.super_type_id)

        #    serializer = SuperSerializer(supers, many=True)

        #    custom_response_dictionary[super.name] = {
        #        "type": super_serializer.data
        #    }
        return Response(custom_response_dictionary)

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
