# Generated by Django 5.1 on 2024-09-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_jobmodel_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='vacancy',
            field=models.PositiveIntegerField(null=True),
        ),
    ]