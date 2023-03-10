# Generated by Django 4.1.5 on 2023-03-12 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cage', '0001_initial'),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rabbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], default='Macho', max_length=1)),
                ('rabbit_tag', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('rabbit_photo', models.ImageField(blank=True, default='rabbit_avatar.png', null=True, upload_to='media/rabbits/', verbose_name='Foto del conejo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_doe', models.BooleanField(default=False)),
                ('is_buck', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.breed')),
                ('cage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cage.cage')),
                ('rabbit_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.rabbitstatus')),
            ],
            options={
                'verbose_name': 'Rabbit',
                'verbose_name_plural': 'Rabbits',
                'default_manager_name': 'objects',
            },
        ),
    ]
