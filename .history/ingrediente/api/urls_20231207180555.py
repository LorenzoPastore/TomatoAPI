from django.urls import path
from ingrediente.api.view import IngredienteCreateAPIView, IngredienteDetailAPIView, IngredienteByRicettaAPIView, IngredienteByRistoranteAPIView

urlpatterns = [
    path("ingredienti/",
         IngredienteCreateAPIView.as_view(),
         name="ingredienti-list"),

    path("ingredienti//<int:pk>/",
         IngredienteDetailAPIView.as_view(),
         name="ingredienti-detail"),

    path("ingredienti_by_ricetta/<int:ricetta_id>/",
         IngredienteByRicettaAPIView.as_view(),
         name="ricette-byricetta"),

    path("ingredienti_by_ristorante/<int:ristorante_id>/",
         IngredienteByRistoranteAPIView.as_view(),
         name="ingredienti-byristorante")
]