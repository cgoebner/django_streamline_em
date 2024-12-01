from django.urls import path
from . import views
from .views import (ph_index_view, ph_add_record_view, ph_add_equipment_view, ph_equipment_view, ph_records_view,
                    ph_test_view)

urlpatterns = [
    path('', ph_index_view, name='index'),
]

urlpatterns += [
    path('records/add-record/', ph_add_record_view, name='add record'),
    path('equipment/add-equipment/', ph_add_equipment_view, name='add equipment'),
    path('equipment/', ph_equipment_view, name='equipment'),
    path('records/', ph_records_view, name='records'),
    path('test/', ph_test_view, name='test'),
]