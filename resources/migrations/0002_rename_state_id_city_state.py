# Generated by Django 4.1.5 on 2023-02-16 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='state_id',
            new_name='state',
        ),
    ]
