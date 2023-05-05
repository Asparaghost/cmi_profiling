from django.contrib import admin
from django.urls import path
from project import views  
 
app_name = 'project'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('projects/PDFs',views.pdf,name='pdf'),
    path('projects/', views.index, name='project'),  
    path('projects/add_Project/',views.add, name='add'),  
    path('projects/<proj_id>/',views.details, name='details'), 
    path('projects/edit/<proj_id>', views.edit, name='edit'),  
    path('projects/delete/<proj_id>/', views.delete, name='delete'),  
    path('report', views.report, name='report'),
    path('projects/pdf/<proj_id>', views.pdf_report_create, name='create-pdf'), 
]