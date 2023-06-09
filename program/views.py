from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProgramForm 
from program.models import Researcher 
from program.models import Program, HistoricalRecords 
from .filters import ProgramFilter, ProgramFilterDB
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def nav(request):
    return render(request, "consortium/nav.html")

def index(request):  
    programs = Program.objects.all()  
    program_filter = ProgramFilter(request.GET, queryset=programs)
    context = {
        'program_filter':program_filter
    }
    return render(request,"program/index.html", context)

@login_required
def pdf(request):  
    programs = Program.objects.all()  
    program_filter = ProgramFilterDB(request.GET, queryset=programs)
    context = {
        'program_filter':program_filter
    }
    return render(request,"program/pdf_page.html", context)  

@login_required
def report(request, prog_id):  
    program = Program.objects.get(prog_id=prog_id)
    budget = program.prog_budg.all()
    projects = program.proj_prog.all()
    context = {
        'program' : program, 'projects' : projects, 'budget' : budget
    }
    return render(request, 'program/report.html',context)

def details(request, prog_id):
    program = Program.objects.get(prog_id=prog_id)
    budget = program.prog_budg.all()
    history_list = Program.history.filter(prog_id=prog_id).order_by('-history_date').distinct()
    projects = program.proj_prog.all()
    context = {
        'program' : program, 'projects' : projects, 'history_list' : history_list, 'budget' : budget,
    }
    return render(request, 'program/details.html',context)

@login_required
def add(request):  
    if request.method == "POST":  
        form = ProgramForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/programs')  
            except:  
                pass
    else:  
        form = ProgramForm()  
    return render(request,'program/add.html',{'form':form})  

@login_required
def edit(request, prog_id):
    program = Program.objects.get(prog_id=prog_id)
    form = ProgramForm(instance = program)  
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance = program)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.modified_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/programs')  
            except:  
                pass
    return render(request, 'program/edit.html', {'form':form})

@login_required
def delete(request, prog_id):  
    program = Program.objects.get(prog_id=prog_id)
    budget = program.prog_budg.all()  
    context = {
            'program' : program,
            'budget' : budget,
    }
    if request.method == 'POST':
            program.delete()
            return redirect('/programs')
    return render(request, 'program/delete.html', context)


# to generate pdf---------------------------------------------

@login_required
def pdf_report_create(request, prog_id):
    program = Program.objects.get(prog_id=prog_id)
    budget = program.prog_budg.all()
    projects = program.proj_prog.all()
    template_path = 'program/report.html'
    context = {
        'program' : program, 'projects' : projects, 'budget' : budget
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Program_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

