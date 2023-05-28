from django.contrib import admin
from django.urls import path
from secretariat import views  
 
app_name = 'secretariat'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('secretariat/PDFs',views.pdf,name='pdf'),
    path('secretariat/', views.index, name='secretariat'),  
    path('secretariat/add_Secretariat/',views.add, name='add'),  
    path('secretariat/<secretariat_id>/',views.details, name='details'), 
    path('secretariat/edit/<secretariat_id>', views.edit, name='edit'),  
    path('secretariat/delete/<secretariat_id>/', views.delete, name='delete'), 
    path('report', views.report, name='report'),
    path('secretariat/pdf/<secretariat_id>', views.pdf_report_create, name='create-pdf'), 
]