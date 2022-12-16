
from django.urls import path
from .views import *

urlpatterns = [
    path('', personDetails, name='home'),
    path('download_pdf/', download, name='download_pdf'),
    path('excel_download/', excelData, name='excel_download'),
]
