# Generated by Django 3.2.16 on 2022-12-21 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beachhouse', '0004_auto_20221221_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beachhouse.owner'),
        ),
        migrations.DeleteModel(
            name='Guests',
        ),
    ]
