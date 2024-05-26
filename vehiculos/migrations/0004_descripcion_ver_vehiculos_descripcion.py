# Generated by Django 5.0.6 on 2024-05-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_precio_ver_vehiculos_valor_dolares'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Estado del Vehículo',
                'verbose_name_plural': 'Estados de los Vehículos',
            },
        ),
        migrations.AddField(
            model_name='ver_vehiculos',
            name='descripcion',
            field=models.CharField(max_length=400, null=True),
        ),
    ]