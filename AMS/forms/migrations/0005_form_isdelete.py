# Generated by Django 5.0.4 on 2024-09-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='IsDelete',
            field=models.BooleanField(default=False),
        ),
    ]
