from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ricetta.models import Ricetta
from ricetta.api.serializers import RicettaSerializer

class RicettaCreateAPIView(APIView):

    def get(self, request):
        ricette = Ricetta.objects.all()
        serializer = RicettaSerializer(ricette, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RicettaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RicettaDetailAPIView(APIView):

    def get_object(self, pk):
        ricetta = get_object_or_404(Ricetta, pk=pk)
        return ricetta
    
    def get(self, request, pk):
        ricetta = self.get_object(pk)
        serializer = RicettaSerializer(ricetta)
        return Response(serializer.data)

    def put(self, request, pk):
        ricetta = self.get_object(pk)
        serializer = RicettaSerializer(ricetta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        ricetta = self.get_object(pk)
        ricetta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RicettaByRistoranteAPIView(APIView):

    def get(self, request, ristorante_id):
        ricette = Ricetta.objects.filter(ristoranti__id=ristorante_id)
        serializer = RicettaSerializer(ricette, many=True)
        return Response(serializer.data)
    
class RicettaByIngredienteAPIView(APIView):

    def get(self, request, ingrediente_id):
        ricette = Ricetta.objects.filter(ingredienti=ingrediente_id)
        serializer = RicettaSerializer(ricette, many=True)
        return Response(serializer.data)