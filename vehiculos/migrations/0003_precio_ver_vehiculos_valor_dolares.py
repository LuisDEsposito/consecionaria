# Generated by Django 5.0.6 on 2024-05-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_alter_ver_vehiculos_marcas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_dolares', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Precio',
                'verbose_name_plural': 'Precios',
            },
        ),
        migrations.AddField(
            model_name='ver_vehiculos',
            name='valor_dolares',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
