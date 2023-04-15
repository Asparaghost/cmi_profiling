from django.contrib import admin
from django.urls import path
from team import views  
 
app_name = 'team'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('teams/PDFs',views.pdf,name='pdf'),
    path('teams/', views.index, name='team'),  
    path('add_Team/',views.add, name='add'),  
    path('teams/<member_id>/',views.details, name='details'), 
    path('teams/edit/<member_id>', views.edit, name='edit'),  
    path('teams/delete/<member_id>/', views.delete, name='delete'),  
    path('report', views.report, name='report'),
    path('teams/pdf/<member_id>', views.pdf_report_create, name='create-pdf'), 
]