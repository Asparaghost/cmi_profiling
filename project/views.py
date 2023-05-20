from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm 
from .models import Project 
from .filters import ProjectFilter, ProjectFilterDB
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def nav(request):
    return render(request, "consortium/nav.html")

def index(request):  
    projects = Project.objects.all()  
    project_filter = ProjectFilter(request.GET, queryset=projects)
    context = {
        'project_filter':project_filter
    }
    return render(request,"project/index.html", context) 

@login_required
def pdf(request):  
    projects = Project.objects.all()  
    project_filter = ProjectFilterDB(request.GET, queryset=projects)
    context = {
        'project_filter':project_filter
    }
    return render(request,"project/pdf_page.html", context)

@login_required
def report(request, proj_id):  
    project = Project.objects.get(proj_id=proj_id)
    proj_imp = project.proj_imp.all()
    proj_output = project.proj_output.all()
    context = {
        'project' : project,
        'proj_imp' : proj_imp,
        'proj_output' : proj_output,
    }
    return render(request, 'project/report.html', context)

def details(request, proj_id):
    project = Project.objects.get(proj_id=proj_id)
    history_list = Project.history.filter(proj_id=proj_id).order_by('-history_date').distinct()
    context = {
        'project' : project, 'history_list' : history_list,
    }
    return render(request, 'project/details.html',context)

@login_required
def add(request):  
    if request.method == "POST":  
        form = ProjectForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/projects')  
            except:  
                pass
    else:  
        form = ProjectForm()  
    return render(request,'project/add.html',{'form':form})  

@login_required
def edit(request, proj_id):
    project = Project.objects.get(proj_id=proj_id)
    form = ProjectForm(instance = project)  
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.modified_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/projects')  
            except:  
                pass
    return render(request, 'project/edit.html', {'form':form})

@login_required
def delete(request, proj_id):  
    project = Project.objects.get(proj_id=proj_id)  
    context = {
            'project' : project,
    }
    if request.method == 'POST':
            project.delete()
            return redirect('/projects')
    return render(request, 'project/delete.html', context)

@login_required
def pdf_report_create(request, proj_id):
    project = Project.objects.get(proj_id=proj_id)
    proj_imp = project.proj_imp.all()
    proj_output = project.proj_output.all()
    template_path = 'project/report.html'
    context = {
        'project' : project,
        'proj_imp' : proj_imp,
        'proj_output' : proj_output,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Project_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

