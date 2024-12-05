from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EquipmentType)
admin.site.register(Period)
admin.site.register(EquipmentManufacturer)
admin.site.register(EquipmentModel)
admin.site.register(Instance)
admin.site.register(RecordType)
admin.site.register(RecordLog)