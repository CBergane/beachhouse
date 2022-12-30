# Generated by Django 3.2.16 on 2022-12-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beachhouse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='user',
        ),
        migrations.AddField(
            model_name='bookings',
            name='user',
            field=models.ManyToManyField(blank=True, to='beachhouse.Guests'),
        ),
    ]
