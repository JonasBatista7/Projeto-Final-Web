# Generated by Django 4.1.3 on 2022-11-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos', '0005_remove_carrinho_nome_carrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='NOME_CARRINHO',
            field=models.CharField(default='Carrinho', max_length=30),
        ),
    ]