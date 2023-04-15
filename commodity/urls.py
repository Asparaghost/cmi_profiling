from django.contrib import admin
from django.urls import path
from commodity import views  
 
app_name = 'commodity'

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('commodities/PDFs',views.pdf,name='pdf'),
    path('commodities/', views.index, name='commodity'),  
    path('commodities/add_Commodity/',views.add_commodity, name='add_commodity'),  
    path('commodities/<name>/',views.details, name='details'), 
    path('commodities/edit/<name>', views.edit, name='edit'),  
    path('commodities/delete/<name>/', views.delete, name='delete'), 
    path('report', views.report, name='report'),
    path('commodities/pdf/<name>', views.pdf_report_create, name='create-pdf'), 
]