# Generated by Django 5.1.3 on 2024-12-01 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0011_alter_equipmentmodel_documents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordlog',
            name='end_date',
            field=models.DateField(blank=True, help_text='Use this end date  to enter dates associated with the detail. (e.g., test end date, maintenance due date etc.)'),
        ),
        migrations.AlterField(
            model_name='recordlog',
            name='references',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='recordlog',
            name='start_date',
            field=models.DateField(blank=True, help_text='Use this start date to enter dates associated with the detail. (e.g., test start date, maintenance due date etc.)'),
        ),
    ]