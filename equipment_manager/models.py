import uuid
from datetime import date

from django.db import models


class EquipmentType(models.Model):
    type = models.CharField(max_length=100, null=False, help_text='Enter the type of the equipment. (e.g., oven, '
                                                                  'tape measure etc.)')

    def __str__(self):
        return self.type


class Period(models.Model):
    """
    This table is to ensure that periods are consistent with the relativedelta function used to
    calculate maintenance and calibration periods.
    """
    period = models.CharField(max_length=50, null=False, help_text='Enter period in plain language. (e.g.,once per year,'
                                                                   ' every 3 months, once per week etc.)')
    rel_period = models.CharField(max_length=20, help_text='Use this field to enter the associated relativedelta value.')

    def __str__(self):
        return f"{self.period} ({self.rel_period})"


class EquipmentManufacturer(models.Model):
    """This table is to ensure manufacturers are referenced consistently"""
    manufacturer = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.manufacturer


class EquipmentModel(models.Model):
    manufacturer = models.ForeignKey(EquipmentManufacturer, null=False, on_delete=models.PROTECT)
    model_sku = models.CharField(max_length=100, null=False)
    maintenance_period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='maintenance', help_text='Maintenance period.')
    calibration_period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='calibration', help_text='Calibration period.')
    type = models.ForeignKey(EquipmentType, null=False, on_delete=models.PROTECT)
    description = models.CharField(max_length=100)
    documents = models.FileField(upload_to='mfg_documents/')
    approval_ref = models.CharField(max_length=50)
    date = models.DateField(default=date.today, null=False)
    by = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.manufacturer} {self.model_sku}"


class Instance(models.Model):
    instance_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eqp_model = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE)
    internal_id = models.CharField(max_length=50, unique=True, null=False)
    serial_number = models.CharField(max_length=50)
    entry_date = models.DateField(default=date.today, null=False)
    by = models.CharField(max_length=50, null=False)

    class Meta:
        ordering = ['internal_id']

    def __str__(self):
        return f"{self.internal_id} - {self.eqp_model}"


class RecordType(models.Model):
    """This table is for controlling the types of records for referential integrity"""
    type = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.type


class RecordDetail(models.Model):
    """This table ties the RecordTypes to specific RecordDetails. For Example a calibration record type would be
    connected to a calibration due record detail. This way the record log would display
    Calibration / Calibration Due or Calibration / Calibration Performed or Maintenance / Maintenance Due
    """
    record_type = models.ForeignKey(RecordType, null=False, on_delete=models.CASCADE)
    detail = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['record_type']

    def __str__(self):
        return f"{self.record_type} - {self.detail}"


class RecordLog(models.Model):
    """This table documents all the records associated with a specific equipment instance. For example a record
    referencing a verification reference would tie the equipment instance to the record.
    """
    record_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instance = models.ForeignKey(Instance, null=False, on_delete=models.CASCADE)
    record_detail = models.ForeignKey(RecordDetail, null=False, on_delete=models.CASCADE)
    details = models.CharField(max_length=400)
    detail_date = models.DateField(default=date.today, help_text='Use this field to enter dates associated with the '
                                                                 'detail. (e.g., calibration due date, maintenance '
                                                                 'due date etc.)')
    documents = models.FileField(upload_to='eqp_records/')
    references = models.CharField(max_length=100)
    entry_date = models.DateField(default=date.today, null=False, help_text='Use this field to record the date of '
                                                                            'this record.')
    by = models.CharField(max_length=50, null=False)

    class Meta:
        ordering = ['instance', 'entry_date']

    def __str__(self):
        return f"{self.instance}  (log id: {self.record_uuid})"