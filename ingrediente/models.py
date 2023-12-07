from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=50, unique = True)
    unita_misura = models.CharField(max_length=50, blank=True)
    quantita = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome