# Generated by Django 4.2.7 on 2023-12-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasAPP', '0003_alter_reserva_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='desc',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
