# Generated by Django 4.1.5 on 2023-03-13 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doe', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doe',
            name='farm',
        ),
    ]
