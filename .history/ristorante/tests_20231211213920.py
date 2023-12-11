from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ristorante.models import Ristorante
from ricetta.models import Ricetta
from ristorante.api.serializers import RistoranteSerializer

class RistoranteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ricetta = Ricetta.objects.create(
            nome='Ricetta Test',
            descrizione='Descrizione Test',
            prezzo=20,
            tempo_preparazione=30,
            difficolta='medio',
        )
        self.ristorante = Ristorante.objects.create(
            nome='Ristorante Test',
            indirizzo='Indirizzo Test',
            proprietario='Proprietario Test',
            email='test@example.com',
        )
        self.ristorante.ricette.add(self.ricetta)

    def test_ristorante_create_api(self):
        data = {
            'nome': 'Nuovo Ristorante',
            'indirizzo': 'Indirizzo Nuovo Ristorante',
            'proprietario': 'Proprietario Nuovo Ristorante',
            'email': 'nuovo@example.com'
        }
        response = self.client.post(reverse('ristorante-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ristorante_detail_api(self):
        response = self.client.get(reverse('ristorante-detail', args=[self.ristorante.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Ristorante Test')

    def test_ristorante_update_api(self):
        data = {
            'nome': 'Ristorante Aggiornato',
            'indirizzo': 'Indirizzo Nuovo Ristorante',
            'proprietario': 'Proprietario Nuovo Ristorante',
            'email': 'nuovo@example.com'
            }
        response = self.client.put(reverse('ristorante-detail', args=[self.ristorante.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ristorante.objects.get(id=self.ristorante.id).nome, 'Ristorante Aggiornato')

    def test_ristorante_delete_api(self):
        response = self.client.delete(reverse('ristorante-detail', args=[self.ristorante.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ristorante_by_ricetta_api(self):
        response = self.client.get(reverse('ristorante-byricetta', args=[self.ricetta.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
