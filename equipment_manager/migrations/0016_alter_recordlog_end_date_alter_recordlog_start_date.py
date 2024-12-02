# Generated by Django 5.1.3 on 2024-12-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0015_alter_recordlog_end_date_alter_recordlog_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordlog',
            name='end_date',
            field=models.DateField(blank=True, default=None, help_text='Use this field to enter the next date calibration or maintenance is due.', null=True, verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='recordlog',
            name='start_date',
            field=models.DateField(blank=True, default=None, help_text='Use this field to enter the date calibration or maintenance was performed.', null=True, verbose_name='Date Performed'),
        ),
    ]
