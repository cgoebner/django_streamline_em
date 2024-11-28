from django.db import models
from datetime import date
import uuid

from django.db.models import PROTECT


class Period(models.Model):
    period = models.CharField(max_length=50, help_text="Enter periods i.e. monthly, weekly, yearly etc.")
    days = models.IntegerField(
        help_text="Enter associated day length of the period. i.e. weeks=7 days, months=30 days, years=365 days etc.")


class EquipmentManufacturer(models.Model):
    manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return self.manufacturer


class EquipmentModel(models.Model):
    manufacturer = models.ForeignKey(EquipmentManufacturer, on_delete=models.PROTECT)
    model = models.CharField(max_length=100)
    maintenance_period = models.ForeignKey(Period, help_text="maintenance period.")
    calibration_period = models.ForeignKey(Period, on_delete=models.PROTECT, help_text="Calibration period.")
    description = models.CharField(max_length=100)
    approval_reference = models.CharField(max_length=50)

    def __str__(self):
        return self.model


class EquipmentInstance(models.Model):
    instance_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE)
    internal_id = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50)
    first_use_date = models.DateField("date", default=date.today)
    calibration_due = models.DateField(help_text="Calibration due date.")

    class Meta:
        ordering = ['internal_id']

    def __str__(self):
        return self.internal_id


class RecordType(models.Model):
    record_type = models.CharField(max_length=60)

    def __str__(self):
        return self.record_type


class EquipmentRecord(models.Model):
    record_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment_instance = models.ForeignKey(EquipmentInstance, on_delete=models.CASCADE)
    record_type = models.ForeignKey(RecordType, on_delete=models.CASCADE)
    details = models.CharField(max_length=400)
    date = models.DateField("date", default=date.today)

    class Meta:
        ordering = ['equipment_instance', 'date']

    def __str__(self):
        return f"{self.equipment_instance} {self.record_uuid}"


class StatusType(models.Model):
    status_type = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.status_type


class EquipmentStatus(models.Model):
    status_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_type = models.ForeignKey(StatusType, on_delete=models.CASCADE)
    equipment_instance = models.ForeignKey(EquipmentInstance, on_delete=models.CASCADE)
    details = models.CharField(max_length=400)
    date = models.DateField("date", default=date.today)

    class Meta:
        ordering = ['equipment_instance', 'date']

    def __str__(self):
        return self.equipment_instance
