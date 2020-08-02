from django.urls import path
from .views import tratamentos,tratamento_detail


urlpatterns = [
    path('tratamentos/',tratamentos, name="tratamentos"),
    path('tratamentos/<int:id>/',tratamento_detail, name="tratamentos_detalhe"),

]