# Generated by Django 3.2.16 on 2023-02-05 19:11

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beachhouse', '0020_auto_20230205_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AlterField(
            model_name='bookings',
            name='checkin',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 2, 5, 19, 11, 19, 792309, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='checkout',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 2, 5, 19, 11, 19, 792337, tzinfo=utc))]),
        ),
    ]
