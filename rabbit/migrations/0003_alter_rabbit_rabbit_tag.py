# Generated by Django 4.1.5 on 2023-02-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0002_alter_rabbit_options_alter_rabbit_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabbit',
            name='rabbit_tag',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]