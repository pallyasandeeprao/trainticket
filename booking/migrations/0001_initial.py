# Generated by Django 4.2.3 on 2023-11-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=70)),
                ('no_of_tickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.IntegerField()),
                ('train_destination', models.CharField(max_length=100)),
                ('no_of_tickets', models.IntegerField()),
                ('date', models.DateField()),
                ('amount', models.CharField(max_length=70)),
            ],
        ),
    ]
