from django.urls import path
from .views import ofertas


urlpatterns = [
    path('ofertas/',ofertas, name="ofertas"),

]