# Generated by Django 4.1.5 on 2023-03-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_alter_diary_costs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='costs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
