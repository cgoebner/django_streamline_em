from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import JsonResponse


def records(request):
    context = {}
    return render(request, 'records.html', context)


def home(request):
    context = {
    }
    return render(request, 'home.html', context)


def modelchoicefield(request):
    form = RecordLogForm(request.POST or None)
    if request.POST and form.is_valid():
        instance = form.cleaned_data['Equipment Instance']
        record_detail = form.cleaned_data['Record Detail']
        start_date = form.cleaned_data['Date Performed/Start Date']
        end_date = form.cleaned_data['Due Date/End Date']
        details = form.cleaned_data['Record Details']
        by = form.cleaned_data['Created By']
        entry_date = form.cleaned_data['Record Entry Date']

        obj = RecordLog(
            instance=instance,
            record_detail=record_detail,
            start_date=start_date,
            end_date=end_date,
            details=details,
            by=by,
            entry_date=entry_date,
        )

        obj.save()
        form2 = RecordLogForm(request.POST, instance=obj)
        form2.save(commit=False)
        form2.save_m2m()
        return redirect('home')

    context = {'form': form}
    return render(request, 'modelchoicefield.html', context)


def jsonrecords(request):
    result_list = list(RecordLog.objects.all() \
                       .values('entry_date',
                               'instance',
                               'record_detail',
                               'details',
                               'start_date',
                               'end_date',
                               'by',
                               'record_uuid',
                               ))

    return JsonResponse(result_list, safe=False)
