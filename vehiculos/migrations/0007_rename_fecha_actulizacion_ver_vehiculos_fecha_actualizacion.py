# Generated by Django 5.0.6 on 2024-05-30 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0006_ver_vehiculos_fecha_actulizacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ver_vehiculos',
            old_name='fecha_actulizacion',
            new_name='fecha_actualizacion',
        ),
    ]
