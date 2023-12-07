from django.db import models
from ingrediente.models import Ingrediente

class Ricetta(models.Model):
    nome = models.CharField(max_length=100, unique = True)
    descrizione = models.TextField(blank=True)
    prezzo = models.PositiveIntegerField(null=True, blank=True)
    tempo_preparazione = models.PositiveIntegerField(null=True, blank=True)
    difficolta = models.CharField(max_length=20, choices=[
        ('facile', 'Facile'),
        ('medio', 'Medio'),
        ('difficile', 'Difficile'),
    ], blank=True)
    ingredienti = models.ManyToManyField(Ingrediente, related_name='ricette', blank=True)

    def __str__(self):
        return self.nome