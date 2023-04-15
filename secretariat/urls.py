from django.contrib import admin
from django.urls import path
from secretariat import views  
 
app_name = 'secretariat'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('secretariats/PDFs',views.pdf,name='pdf'),
    path('secretariats/', views.index, name='secretariat'),  
    path('secretariats/add_Secretariat/',views.add, name='add'),  
    path('secretariats/<secretariat_id>/',views.details, name='details'), 
    path('secretariats/edit/<secretariat_id>', views.edit, name='edit'),  
    path('secretariats/delete/<secretariat_id>/', views.delete, name='delete'), 
    path('report', views.report, name='report'),
    path('secretariats/pdf/<secretariat_id>', views.pdf_report_create, name='create-pdf'), 
]