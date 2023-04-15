from django.contrib import admin
from django.urls import path
from consortium import views  
 
app_name = 'consortium'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('CMIs/PDFs',views.pdf,name='pdf'),
    path('CMIs/', views.index, name='cmi'),  
    path('CMIs/add_CMI/',views.add, name='add'),  
    path('CMIs/<name>/',views.details, name='details'), 
    path('CMIs/edit/<name>', views.edit, name='edit'),  
    path('CMIs/delete/<name>/', views.delete, name='delete'), 
    path('report', views.report, name='report'),
    path('CMIs/pdf/<name>', views.pdf_report_create, name='create-pdf'), 
]