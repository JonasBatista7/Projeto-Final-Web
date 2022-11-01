from django.contrib import admin
from .models import Produto, Carrinho, Pedidos
# Register your models here.


admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(Pedidos)
