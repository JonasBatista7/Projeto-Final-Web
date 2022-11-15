# Generated by Django 4.1.3 on 2022-11-15 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos', '0009_remove_carrinho_id_produto_carrinho_id_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='QUANTIDADE',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='SUB_TOTAL',
        ),
        migrations.CreateModel(
            name='Produto_Quantidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUANTIDADE', models.IntegerField()),
                ('SUB_TOTAL', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ID_CARRINHO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produtos.carrinho')),
                ('ID_PRODUTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produtos.produto')),
            ],
        ),
    ]
