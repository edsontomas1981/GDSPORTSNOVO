# Generated by Django 4.2 on 2023-05-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.AlterModelOptions(
            name='dados_loja',
            options={'verbose_name': 'Dados da Loja', 'verbose_name_plural': 'Dados das Lojas'},
        ),
    ]
