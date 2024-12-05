from django import forms
from django.forms import ModelForm
from .models import *


class RecordLogForm(ModelForm):
    instance = forms.ModelChoiceField(label='Equipment Instance', queryset=Instance.objects, empty_label=None)
    record_detail = forms.ModelChoiceField(label='Record Detail', queryset=RecordDetail.objects, empty_label=None)
    start_date = forms.DateField(label='Date Performed/Start Date', required=False)
    end_date = forms.DateField(label='Due Date/End Date', required=False)
    details = forms.CharField(label='Record Details', required=True)
    by = forms.CharField(label='Created By', required=True)
    entry_date = forms.DateTimeField(label='Record Entry Date', required=True)

    class Meta:
        model = RecordLog
        fields = '__all__'
