from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ristorante.models import Ristorante
from ristorante.api.serializers import RistoranteSerializer

class RistoranteCreateAPIView(APIView):

    def get(self, request):
        ristoranti = Ristorante.objects.all()
        serializer = RistoranteSerializer(ristoranti, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RistoranteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RistoranteDetailAPIView(APIView):

    def get_object(self, pk):
        ristorante = get_object_or_404(Ristorante, pk=pk)
        return ristorante
    
    def get(self, request, pk):
        ristorante = self.get_object(pk)
        serializer = RistoranteSerializer(ristorante)
        return Response(serializer.data)

    def put(self, request, pk):
        ristorante = self.get_object(pk)
        serializer = RistoranteSerializer(ristorante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        ristorante = self.get_object(pk)
        ristorante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RistoranteByRicettaAPIView(APIView):

    def get(self, request, ricetta_id):
        ristoranti = Ristorante.objects.filter(ricette=ricetta_id)
        serializer = RistoranteSerializer(ristoranti, many=True)
        return Response(serializer.data)