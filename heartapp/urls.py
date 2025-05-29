from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('results/', results,name='results'),
    path('details/', details,name='details'),
    path('risk/',risk,name='risk'),
    path('export_to_csv/',export_to_csv,name='export_to_csv'),  #for add user input to csv file
    path('export/',export_view,name='export'), 
    
]

