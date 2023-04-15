from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CMIForm 
from consortium.models import CMI 
from .filters import CMIFilter
from commodity.models import Commodity 
from program.models import Program
from project.models import Project
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.


def nav(request):
    cmis = CMI.objects.all()  
    return render(request, "consortium/nav.html", {'cmis':cmis})

def index(request):  
    cmis = CMI.objects.all()  
    return render(request,"consortium/index.html",{'cmis':cmis}) 

@login_required
def pdf(request):  
    cmis = CMI.objects.all()    
    cmi_filter = CMIFilter(request.GET, queryset=cmis)
    context = {
        'cmi_filter':cmi_filter
    }
    return render(request,"consortium/pdf_page.html", context)

@login_required
def report(request, name):  
    cmi = CMI.objects.get(name=name)  
    commodities = cmi.commodities.all()
    programs = cmi.programs.all()
    projects = cmi.projects.all()
    context = {
        'cmi' : cmi, 
        'commodities' : commodities, 
        'programs' : programs, 
        'projects' : projects,
    }
    return render(request,"consortium/report.html", context) 

def details(request, name):
    cmi = CMI.objects.get(name=name)
    commodities = cmi.commodities.all()
    programs = cmi.programs.all()
    projects = cmi.projects.all()
    context = {
        'cmi' : cmi, 
        'commodities' : commodities, 
        'programs' : programs, 
        'projects' : projects,
    }
    return render(request, 'consortium/details.html',context)

@login_required
def add(request):  
    if request.method == "POST":  
        form = CMIForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                return redirect('/CMIs')  
            except:  
                pass
    else:  
        form = CMIForm()  
    return render(request,'consortium/add.html',{'form':form})  

@login_required
def edit(request, name):
    cmi = CMI.objects.get(name=name)
    form = CMIForm(instance = cmi)  
    if request.method == 'POST':
        form = CMIForm(request.POST, request.FILES, instance = cmi)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.modified_by = request.user
                instance.save()
                return redirect('/CMIs')  
            except:  
                pass
    return render(request, 'consortium/edit.html', {'form':form})

@login_required
def delete(request, name):  
    cmi = CMI.objects.get(name=name)  
    context = {
            'cmi' : cmi,
    }
    if request.method == 'POST':
            cmi.delete()
            return redirect('/CMIs')
    return render(request, 'consortium/delete.html', context)

@login_required
def pdf_report_create(request, name):
    cmi = CMI.objects.get(name=name)
    commodities = cmi.commodities.all()
    programs = cmi.programs.all()
    projects = cmi.projects.all()
    template_path = 'consortium/report.html'
    context = {
        'cmi' : cmi, 
        'commodities' : commodities, 
        'programs' : programs, 
        'projects' : projects,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="CMI_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

