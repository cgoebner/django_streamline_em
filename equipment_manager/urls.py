
from django.urls import path
from equipment_manager import views as view


urlpatterns = [
    path('', view.home, name='home'),
    path('records/', view.records, name='records'),
    path('modelchoicefield/', view.modelchoicefield, name='modelchoicefield'),
    path('jsonresponse/records', view.jsonrecords, name='jsonrecords'),
]
