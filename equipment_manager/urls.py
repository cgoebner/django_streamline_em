from django.urls import path
from . import views
from .views import ph_index_view

urlpatterns = [
    path('', ph_index_view, name='index'),
]
