# Generated by Django 4.1 on 2023-12-13 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_alter_maquina_condicionn_alter_maquina_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='condiciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicion', models.CharField(max_length=80, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Clases de maquina',
                'verbose_name_plural': 'Clases de maquinas',
            },
        ),
        migrations.CreateModel(
            name='estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=80, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Clases de maquina',
                'verbose_name_plural': 'Clases de maquinas',
            },
        ),
        migrations.AlterField(
            model_name='maquina',
            name='condicionn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.condiciones'),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.estados'),
        ),
    ]