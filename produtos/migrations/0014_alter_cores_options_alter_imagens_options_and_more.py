# Generated by Django 4.2 on 2023-05-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0013_alter_categoria_options_alter_subcategoria_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cores',
            options={'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='imagens',
            options={'verbose_name_plural': 'Imagens'},
        ),
        migrations.AlterModelOptions(
            name='marcas',
            options={'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='produtos',
            options={'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='tamanhos',
            options={'verbose_name_plural': 'Tamanhos'},
        ),
        migrations.RemoveField(
            model_name='subcategoria',
            name='categoria_fk',
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='categoria_fk',
            field=models.ManyToManyField(blank=True, to='produtos.categoria'),
        ),
    ]
