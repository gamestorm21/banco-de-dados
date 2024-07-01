# No arquivo ecommerce_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    # Adicione outras URLs conforme necessário
]
