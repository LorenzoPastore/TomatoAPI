from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ingrediente.models import Ingrediente
from ingrediente.api.serializers import IngredienteSerializer

class IngredienteCreateAPIView(APIView):

    def get(self, request):
        ingredienti = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredienti, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IngredienteDetailAPIView(APIView):

    def get_object(self, pk):
        ingrediente = get_object_or_404(Ingrediente, pk=pk)
        return ingrediente
    
    def get(self, request, pk):
        ingrediente = self.get_object(pk)
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    def put(self, request, pk):
        ingrediente = self.get_object(pk)
        serializer = IngredienteSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        ingrediente = self.get_object(pk)
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class IngredienteByRicettaAPIView(APIView):

    def get(self, request, ricetta_id):
        ingrediente = Ingrediente.objects.filter(ricette__id=ricetta_id)
        serializer = IngredienteSerializer(ingrediente, many=True)
        return Response(serializer.data)
    
class IngredienteByRistoranteAPIView(APIView):

    def get(self, request, ristorante_id):
        ingrediente = Ingrediente.objects.filter(ricette__ristoranti__id=ristorante_id)
        serializer = IngredienteSerializer(ingrediente, many=True)
        return Response(serializer.data)