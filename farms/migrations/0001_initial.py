# Generated by Django 4.1.7 on 2023-04-09 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProducerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Producer profile')),
                ('farm_name', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('is_producer', models.BooleanField(default=False)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.city')),
            ],
        ),
    ]
