# Generated by Django 4.1.3 on 2022-11-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos', '0012_remove_carrinho_id_produto_carrinho_id_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='IMAGEM',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]