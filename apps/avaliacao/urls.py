from django.urls import path
from .views import avaliacao


urlpatterns = [
    path('avaliacao/',avaliacao, name="avaliacao"),

]