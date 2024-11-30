from django.shortcuts import render

# Create your views here.
def ph_index_view(request):
    context = {
        'ph_index_text': 'This is a placeholder for the add states page.'
    }
    return render(request, 'index.html', context)