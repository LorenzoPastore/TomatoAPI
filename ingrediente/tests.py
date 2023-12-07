from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ingrediente.models import Ingrediente
from ricetta.models import Ricetta
from ristorante.models import Ristorante
from ingrediente.api.serializers import IngredienteSerializer

class IngredienteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ristorante = Ristorante.objects.create(nome='Ristorante Test', indirizzo='Indirizzo Test')
        self.ricetta = Ricetta.objects.create(
            nome='Ricetta Test',
            descrizione='Descrizione Test',
            prezzo=20,
            tempo_preparazione=30,
            difficolta='medio'
        )
        self.ingrediente = Ingrediente.objects.create(
            nome='Ingrediente Test',
            unita_misura='g',
            quantita=100
        )
        self.ingrediente.ricette.add(self.ricetta)

    def test_ingrediente_create_api(self):
        data = {
            'nome': 'Nuovo Ingrediente',
            'unita_misura': 'ml',
            'quantita': 150
        }
        response = self.client.post(reverse('ingredienti-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingrediente.objects.count(), 2)

    def test_ingrediente_detail_api(self):
        response = self.client.get(reverse('ingredienti-detail', args=[self.ingrediente.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Ingrediente Test')

    def test_ingrediente_update_api(self):
        data = {'nome': 'Ingrediente Aggiornato'}
        response = self.client.put(reverse('ingredienti-detail', args=[self.ingrediente.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ingrediente.objects.get(id=self.ingrediente.id).nome, 'Ingrediente Aggiornato')

    def test_ingrediente_delete_api(self):
        response = self.client.delete(reverse('ingredienti-detail', args=[self.ingrediente.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ingrediente.objects.count(), 0)

    def test_ingrediente_by_ricetta_api(self):
        response = self.client.get(reverse('ricette-byricetta', args=[self.ricetta.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ingrediente_by_ristorante_api(self):
        response = self.client.get(reverse('ingredienti-byristorante', args=[self.ristorante.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
