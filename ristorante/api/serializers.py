from rest_framework import serializers
from ristorante.models import Ristorante

class RistoranteSerializer(serializers.ModelSerializer):
    
    ricette = serializers.SerializerMethodField('get_ricette')

    def get_ricette(self,obj):
        return [ricette.nome for ricette in obj.ricette.all()]

    class Meta:
        model = Ristorante
        fields = "__all__"