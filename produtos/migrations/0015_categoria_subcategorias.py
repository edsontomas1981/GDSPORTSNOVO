# Generated by Django 4.2 on 2023-05-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0014_alter_cores_options_alter_imagens_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='subcategorias',
            field=models.ManyToManyField(blank=True, to='produtos.subcategoria'),
        ),
    ]