from django import forms 
from .models import *
  
class ProdutoForm(forms.ModelForm): 
  
    class Meta: 
        model = Produto 
        fields = ['NOME_PRODUTO', 'VALOR', 'QUANTIDADE_ESTOQUE','DESCRICAO','IMAGEM'] 