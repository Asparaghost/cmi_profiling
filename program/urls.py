from django.contrib import admin
from django.urls import path
from program import views  
 
app_name = 'program'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('programs/PDFs',views.pdf,name='pdf'),
    path('programs/', views.index, name='program'),  
    path('programs/add_Program/',views.add, name='add'),  
    path('programs/<title>/',views.details, name='details'), 
    path('programs/edit/<title>', views.edit, name='edit'),  
    path('programs/delete/<title>/', views.delete, name='delete'),  
    path('report', views.report, name='report'),
    path('programs/pdf/<title>', views.pdf_report_create, name='create-pdf'), 
]