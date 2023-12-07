from django.urls import path
from ricetta.api.view import RicettaCreateAPIView, RicettaDetailAPIView, RicettaByRistoranteAPIView, RicettaByIngredienteAPIView

urlpatterns = [
    path("ricette/",
         RicettaCreateAPIView.as_view(),
         name="ricette-list"),

    path("ricette//<int:pk>/",
         RicettaDetailAPIView.as_view(),
         name="ricette-detail"),

    path("ricette/ristorante/<int:ristorante_id>/",
         RicettaByRistoranteAPIView.as_view(),
         name="ricette-byristorante"),

    path("ricette_by_ingrediente/<int:ingrediente_id>/",
         RicettaByIngredienteAPIView.as_view(),
         name="ricette-byingrediente")
]