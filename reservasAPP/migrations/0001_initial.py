# Generated by Django 4.2.7 on 2023-12-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=13)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('size', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]