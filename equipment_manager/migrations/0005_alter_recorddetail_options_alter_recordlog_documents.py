# Generated by Django 5.1.3 on 2024-11-30 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0004_alter_equipmentmodel_documents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recorddetail',
            options={'ordering': ['record_type']},
        ),
        migrations.AlterField(
            model_name='recordlog',
            name='documents',
            field=models.FileField(upload_to='eqp_records/'),
        ),
    ]