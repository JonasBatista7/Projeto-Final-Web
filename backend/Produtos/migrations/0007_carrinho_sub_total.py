# Generated by Django 4.1.3 on 2022-11-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos', '0006_carrinho_nome_carrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='SUB_TOTAL',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
