from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ricetta.models import Ricetta
from ingrediente.models import Ingrediente
from ristorante.models import Ristorante
from ricetta.api.serializers import RicettaSerializer

class RicettaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ingrediente = Ingrediente.objects.create(nome='Ingrediente Test')
        self.ricetta = Ricetta.objects.create(
            nome='Ricetta Test',
            descrizione='Descrizione Test',
            prezzo=20,
            tempo_preparazione=30,
            difficolta='medio',
        )
        self.ricetta.ingredienti.add(self.ingrediente)
        self.ristorante = Ristorante.objects.create(
            nome='Ristorante Test',
            indirizzo='Indirizzo Test',
            proprietario='Proprietario Test',
            email='test@example.com',
        )
        self.ristorante.ricette.add(self.ricetta)

    def test_ricetta_create_api(self):
        data = {
            'nome': 'Nuova Ricetta',
            'descrizione': 'Descrizione Nuova Ricetta',
            'prezzo': 25,
            'tempo_preparazione': 45,
            'difficolta': 'difficile',
            'ingredienti': [self.ingrediente.id]
        }
        response = self.client.post(reverse('ricette-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ricetta.objects.count(), 2)

    def test_ricetta_detail_api(self):
        response = self.client.get(reverse('ricette-detail', args=[self.ricetta.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Ricetta Test')

    def test_ricetta_update_api(self):
        data = {'nome': 'Ricetta Aggiornata'}
        response = self.client.put(reverse('ricette-detail', args=[self.ricetta.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ricetta.objects.get(id=self.ricetta.id).nome, 'Ricetta Aggiornata')

    def test_ricetta_delete_api(self):
        response = self.client.delete(reverse('ricette-detail', args=[self.ricetta.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ricetta.objects.count(), 0)

    def test_ricetta_by_ristorante_api(self):
        response = self.client.get(reverse('ricette-byristorante', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ricetta_by_ingrediente_api(self):
        response = self.client.get(reverse('ricette-byingrediente', args=[self.ingrediente.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
