from django.contrib import admin

from equipment_manager.models import EquipmentType, Period, EquipmentManufacturer, EquipmentModel, Instance, RecordType, \
    RecordDetail, RecordLog


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(EquipmentManufacturer)
class EquipmentManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(EquipmentModel)
class EquipmentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(RecordType)
class RecordTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(RecordDetail)
class RecordDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(RecordLog)
class RecordLogAdmin(admin.ModelAdmin):
    pass


