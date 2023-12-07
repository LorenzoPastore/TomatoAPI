from django.urls import path
from ristorante.api.view import RistoranteCreateAPIView, RistoranteDetailAPIView, RistoranteByRicettaAPIView

urlpatterns = [
    path("ristoranti/",
         RistoranteCreateAPIView.as_view(),
         name="ristorante-list"),

    path("ristoranti//<int:pk>/",
         RistoranteDetailAPIView.as_view(),
         name="ristorante-detail"),

    path("ristoranti//<int:ricetta_id>/",
         RistoranteByRicettaAPIView.as_view(),
         name="ristorante-byricetta")

]