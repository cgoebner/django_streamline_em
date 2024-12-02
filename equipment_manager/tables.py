import django_tables2 as tables
from .models import RecordLog

class RecordLogTable(tables.Table):
    class Meta:
        model = RecordLog
        template_name = "django_tables2/bootstrap.html"
        fields = ('instance','entry_date', 'record_detail', 'start_date', 'end_date', 'details', 'by')