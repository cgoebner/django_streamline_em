from django.shortcuts import render
import django_filters
def ph_index_view(request):
    context = {
        'ph_index_text': 'This is a placeholder for the index page.'
    }
    return render(request, 'index.html', context)


def ph_add_record_view(request):
    context = {
        'ph_add_record_text': 'This is a placeholder for the add record page.'
    }
    return render(request, 'add_record.html', context)

def ph_add_equipment_view(request):
    context = {
        'ph_add_equipment_text': 'This is a placeholder for the add equipment page.'
    }
    return render(request, 'add_equipment.html', context)

def ph_records_view(request):
    context = {
        'ph_records_text': 'This is a placeholder for the records page.'
    }
    return render(request, 'records.html', context)

def ph_equipment_view(request):
    context = {
        'ph_equipment_text': 'This is a placeholder for the equipment page.'
    }
    return render(request, 'equipment.html', context)

def ph_test_view(request):
    context = {
        'ph_test_text': 'This is a placeholder for the test page.'
    }
    return render(request, 'test.html', context)


from django_tables2 import SingleTableView
from .models import RecordLog
from .tables import RecordLogTable

class RecordLogListView(SingleTableView):
    model = RecordLog
    table_class = RecordLogTable
    template_name = 'records.html'

# class RecordLogFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = RecordLog
#         fields = ['instance']
#
# def record_log_list(request):
#     f = RecordLogFilter(request.GET, queryset=RecordLog.objects.all())
#     return render(request, 'records.html', {'filter': f})
#
#
# class RecordLogListView:
#     pass