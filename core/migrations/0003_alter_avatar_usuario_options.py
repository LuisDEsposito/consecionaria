# Generated by Django 5.0.4 on 2024-06-04 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_avatar_usuario_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avatar_usuario',
            options={'verbose_name': 'Avatar de usuario', 'verbose_name_plural': 'Avatares de usuarios'},
        ),
    ]
