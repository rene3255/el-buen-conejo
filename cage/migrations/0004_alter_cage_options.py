# Generated by Django 4.1.5 on 2023-02-17 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cage', '0003_rename_farm_id_cage_farm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cage',
            options={'verbose_name': 'Lista de Jaulas', 'verbose_name_plural': 'Total de Jaulas'},
        ),
    ]