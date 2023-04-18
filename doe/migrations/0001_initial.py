# Generated by Django 4.1.7 on 2023-04-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doe_name', models.CharField(max_length=50)),
                ('selection_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Doe',
                'verbose_name_plural': 'Does',
                'default_manager_name': 'objects',
            },
        ),
    ]
