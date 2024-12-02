# Generated by Django 5.1.3 on 2024-12-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0013_alter_recordlog_end_date_alter_recordlog_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordlog',
            name='end_date',
            field=models.DateField(blank=True, default=None, help_text='Use this end date  to enter dates associated with the detail. (e.g., test end date, maintenance due date etc.)', null=True, verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='recordlog',
            name='start_date',
            field=models.DateField(blank=True, default=None, help_text='Use this start date to enter dates associated with the detail. (e.g., test start date, maintenance due date etc.)', null=True, verbose_name='Date Performed'),
        ),
    ]
