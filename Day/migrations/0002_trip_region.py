# Generated by Django 2.0.13 on 2019-05-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Day', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='region',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
