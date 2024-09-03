from django.urls import path
from .apps import SecondTaskConfig
from .views import export_csv

app_name = SecondTaskConfig.name

urlpatterns = [
    path('export_csv/', export_csv, name='export_csv')
]
