# Generated by Django 5.1.3 on 2024-11-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='duration',
            field=models.IntegerField(help_text='Enter the integer value associated with the period.', null=True),
        ),
    ]
