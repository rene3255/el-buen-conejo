# Generated by Django 4.1.5 on 2023-03-12 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cage', '0001_initial'),
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cage',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cages', to='farms.producerprofile'),
        ),
    ]
