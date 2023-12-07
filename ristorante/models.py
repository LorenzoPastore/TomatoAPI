from django.db import models
from ricetta.models import Ricetta

class Ristorante(models.Model):
    nome = models.CharField(max_length=200, unique = True)
    indirizzo = models.CharField(max_length=200)
    proprietario = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    ricette = models.ManyToManyField(Ricetta, related_name='ristoranti', blank=True)
    data_creazione = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome