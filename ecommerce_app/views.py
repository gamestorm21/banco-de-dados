# No arquivo ecommerce_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Pedido, ItemPedido

@login_required
def adicionar_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    # Lógica para adicionar o produto ao carrinho
    # Exemplo simplificado: criar um pedido se não existir um em aberto para o usuário
    pedido, created = Pedido.objects.get_or_create(usuario=request.user, status='aberto')
    ItemPedido.objects.create(produto=produto, pedido=pedido, quantidade=1, subtotal=produto.preco)
    return redirect('carrinho')

@login_required
def finalizar_compra(request):
    # Lógica para finalizar a compra
    return render(request, 'finalizar_compra.html')
