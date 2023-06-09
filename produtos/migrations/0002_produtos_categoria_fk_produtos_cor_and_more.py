# Generated by Django 4.2 on 2023-04-04 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='categoria_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria'),
        ),
        migrations.AddField(
            model_name='produtos',
            name='cor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='marca',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='obs',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='preco',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='subcategoria_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.subcategoria'),
        ),
        migrations.AddField(
            model_name='produtos',
            name='tamanho',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
