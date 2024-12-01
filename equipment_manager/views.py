from django.shortcuts import render

# Create your views here.
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