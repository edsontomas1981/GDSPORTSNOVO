# Generated by Django 4.2 on 2023-04-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_alter_produtos_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='qtde',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(max_length=30, null=True),
        ),
    ]