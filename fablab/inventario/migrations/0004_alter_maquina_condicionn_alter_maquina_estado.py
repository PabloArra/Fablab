# Generated by Django 4.1 on 2023-12-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_maquina_condicionn_alter_maquina_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='condicionn',
            field=models.CharField(blank=True, choices=[{'Libre', 'Disponible'}, {'En uso', 'No disponible'}], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='estado',
            field=models.CharField(blank=True, choices=[{'Funcionando', 'Buen estado'}, {'Dañado', 'Mal estado'}], max_length=40, null=True),
        ),
    ]
