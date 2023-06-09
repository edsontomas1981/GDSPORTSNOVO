# Generated by Django 4.2 on 2023-05-06 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_produtos_qtde_alter_produtos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produtos')),
            ],
        ),
    ]
