# Generated by Django 3.2.16 on 2023-01-17 09:14

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beachhouse', '0013_auto_20230110_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='checkin',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 1, 17, 9, 14, 49, 948208, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='checkout',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 1, 17, 9, 14, 49, 948252, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='house',
            name='capacity',
            field=models.IntegerField(default=0, verbose_name='Number Of Guests'),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='House Owner'),
        ),
    ]
