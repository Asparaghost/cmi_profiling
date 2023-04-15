from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .filters import SecretariatFilter
from .models import Secretariat
from .forms import SecretariatForm
from consortium.models import CMI 
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.


def nav(request):
    cmi = CMI.objects.all()  
    return render(request, "consortium/nav.html", {'cmi':cmi })

def index(request):  
    secretariats = Secretariat.objects.all()  
    return render(request,"secretariat/index.html",{'secretariats':secretariats}) 

@login_required
def pdf(request):  
    secretariats = Secretariat.objects.all()   
    secretariat_filter = SecretariatFilter(request.GET, queryset=secretariats)
    context = {
        'secretariat_filter':secretariat_filter
    }
    return render(request,"secretariat/pdf_page.html", context) 

@login_required
def report(request):  
    secretariats = Secretariat.objects.all()  
    return render(request,"secretariat/report.html",{'secretariats':secretariats}) 

def details(request, secretariat_id):
    secretariat = Secretariat.objects.get(secretariat_id=secretariat_id)
    context = {
        'secretariat' : secretariat,
    }
    return render(request, 'secretariat/details.html', context)

@login_required
def add(request):  
    if request.method == "POST":  
        form = SecretariatForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                return redirect('/secretariats')  
            except:  
                pass
    else:  
        form = SecretariatForm()  
    return render(request,'secretariat/add.html',{'form':form})  

@login_required
def edit(request, secretariat_id):
    secretariat = Secretariat.objects.get(secretariat_id=secretariat_id)
    form = SecretariatForm(instance = secretariat)  
    if request.method == 'POST':
        form = SecretariatForm(request.POST, request.FILES, instance = secretariat)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.modified_by = request.user
                instance.save()
                return redirect('/secretariats')  
            except:  
                pass
    return render(request, 'secretariat/edit.html', {'form':form})

@login_required
def delete(request, secretariat_id):  
    secretariat = Secretariat.objects.get(secretariat_id=secretariat_id)  
    context = {
            'secretariat' : secretariat,
    }
    if request.method == 'POST':
            secretariat.delete()
            return redirect('/secretariats')
    return render(request, 'secretariat/delete.html', context)

@login_required
def pdf_report_create(request, secretariat_id):
    secretariat = Secretariat.objects.get(secretariat_id=secretariat_id)
    template_path = 'secretariat/report.html'
    context = {'secretariat': secretariat}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Secretariat_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

