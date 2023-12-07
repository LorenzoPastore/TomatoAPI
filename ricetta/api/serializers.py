from rest_framework import serializers
from ricetta.models import Ricetta

class RicettaSerializer(serializers.ModelSerializer):

    ingredienti = serializers.SerializerMethodField('get_ingredienti')

    def get_ingredienti(self,obj):
        return [ingredienti.nome for ingredienti in obj.ingredienti.all()]

    class Meta:
        model = Ricetta
        fields = "__all__"