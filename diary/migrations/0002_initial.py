# Generated by Django 4.1.7 on 2023-04-18 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farms', '0001_initial'),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.producerprofile'),
        ),
    ]
