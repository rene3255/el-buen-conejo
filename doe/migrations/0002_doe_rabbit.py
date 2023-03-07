# Generated by Django 4.1.5 on 2023-03-06 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0006_alter_rabbit_rabbit_photo'),
        ('doe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doe',
            name='rabbit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rabbit.rabbit'),
        ),
    ]