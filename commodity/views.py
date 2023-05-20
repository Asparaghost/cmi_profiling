from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommodityForm, IecMaterialForm
from commodity.models import Commodity, IecMaterial
from .filters import CommodityFilter, CommodityFilterDB
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.


def nav(request):
     return render(request, "commodity/nav.html")

def index(request):  
    commodities = Commodity.objects.all()  
    commodity_filter = CommodityFilter(request.GET, queryset=commodities)
    context = {
        'commodity_filter':commodity_filter
    }
    return render(request,"commodity/index.html", context) 

@login_required
def pdf(request):  
    commodities = Commodity.objects.all()  
    commodity_filter = CommodityFilterDB(request.GET, queryset=commodities)
    context = {
        'commodity_filter':commodity_filter
    }
    return render(request,"commodity/pdf_page.html", context)

@login_required
def report(request):  
    commodities = Commodity.objects.all()  
    return render(request,"commodity/report.html",{'commodities':commodities}) 

def details(request, name):
    commodity = Commodity.objects.get(name=name)
    iecmaterials = commodity.iecmaterials.all()
    adaptors = commodity.adaptor.all()
    programs = commodity.prog_com.all()
    projects = commodity.proj_com.all()
    context = {
        'commodity' : commodity, 
        'iecmaterials' : iecmaterials, 
        'programs' : programs,
        'projects' : projects,
        'adaptors' : adaptors,
    }
    return render(request, 'commodity/details.html',context)

@login_required
def add_commodity(request):  
    if request.method == "POST":  
        form = CommodityForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/commodities')  
            except:  
                pass
    else:  
        form = CommodityForm()  
    return render(request,'commodity/add_commodity.html',{'form':form})  


@login_required
def edit(request, name):
    commodity = Commodity.objects.get(name=name)
    form = CommodityForm(instance = commodity)  
    if request.method == 'POST':
        form = CommodityForm(request.POST, request.FILES, instance = commodity)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.modified_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/commodities')  
            except:  
                pass
    return render(request, 'commodity/edit.html', {'form':form})

@login_required
def delete(request, name):  
    commodity = Commodity.objects.get(name=name)  
    context = {
            'commodity' : commodity,
    }
    if request.method == 'POST':
            commodity.delete()
            return redirect('/commodities')
    return render(request, 'commodity/delete.html', context)


# to generate pdf---------------------------------------------

@login_required
def pdf_report_create(request, name):
    commodity = Commodity.objects.get(name=name)
    iecmaterials = commodity.iecmaterials.all()
    adaptors = commodity.adaptor.all()
    programs = commodity.prog_com.all()
    projects = commodity.proj_com.all()
    template_path = 'commodity/report.html'
    context = {
        'commodity': commodity,
        'iecmaterials': iecmaterials,
        'programs' : programs,
        'projects' : projects,
        'adaptors' : adaptors,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Commodity_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

