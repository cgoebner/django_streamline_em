# Generated by Django 5.1.3 on 2024-12-01 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0008_alter_period_rel_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordlog',
            name='detail_date',
        ),
        migrations.AddField(
            model_name='recordlog',
            name='end_date',
            field=models.DateField(default=datetime.date.today, help_text='Use this end date  to enter dates associated with the detail. (e.g., test end date, maintenance due date etc.)'),
        ),
        migrations.AddField(
            model_name='recordlog',
            name='start_date',
            field=models.DateField(default=datetime.date.today, help_text='Use this start date to enter dates associated with the detail. (e.g., test start date, maintenance due date etc.)'),
        ),
    ]
