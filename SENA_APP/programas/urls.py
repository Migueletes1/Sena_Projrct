from django.urls import path You, 12 hours ago • Include Prop  
from . import views  
  
app_name = 'programas'  
  
urlpatterns = [  
    path('programas/', views.programas, name='lista_programas'),  
]  