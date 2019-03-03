from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .import serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):
    """Test API View."""
    
    serializer_class = serializers.HelloSerializer
   

    def get(self, request, format=None):
        """Returns a llist of APIView Features."""

        an_apiview = [
            'Uses HTTP methods as function(get,post,put,delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over Logic',
            'It mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})



    def post(self, request):
        """create a hello message with our name"""


        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message  = 'Hello {0}'.format(name)

            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  



    def put(self, request, pk=None):
        """Handles Updating an Object"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Updates field provided int therequest"""

        return Response({'method':'patch'})
        
    def delete(self, request, pk=None):
        """Deletes an  Object"""

        return Response({'method':'delete'})        


