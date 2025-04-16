# Generated by Django 5.2 on 2025-04-16 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_autores', '0003_delete_frase'),
        ('app_frases', '0002_frase_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frase',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frases', to='app_autores.autor'),
        ),
    ]
