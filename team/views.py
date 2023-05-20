from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeamForm 
from .models import Team
from .filters import TeamFilter, TeamFilterDB
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def nav(request):
    return render(request, "consortium/nav.html")

def index(request):  
    teams = Team.objects.all()  
    team_filter = TeamFilter(request.GET, queryset=teams)
    context = {
        'team_filter':team_filter
    }
    return render(request,"team/index.html", context) 

@login_required
def pdf(request):  
    teams = Team.objects.all()  
    team_filter = TeamFilterDB(request.GET, queryset=teams)
    context = {
        'team_filter':team_filter
    }
    return render(request,"team/pdf_page.html", context) 

@login_required
def report(request):  
    teams = Team.objects.all()  
    return render(request,"team/report.html",{'teams':teams}) 

def details(request, member_id):
    team = Team.objects.get(member_id=member_id)
    context = {
        'team' : team,
    }
    return render(request, 'team/details.html',context)

@login_required
def add(request):  
    if request.method == "POST":  
        form = TeamForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/teams')  
            except:  
                pass
    else:  
        form = TeamForm()  
    return render(request,'team/add.html',{'form':form})  

@login_required
def edit(request, member_id):
    team = Team.objects.get(member_id=member_id)
    form = TeamForm(instance = team)  
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance = team)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.modified_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/teams')  
            except:  
                pass
    return render(request, 'team/edit.html', {'form':form})

@login_required
def delete(request, member_id):  
    team = Team.objects.get(member_id=member_id)  
    context = {
            'team' : team,
    }
    if request.method == 'POST':
            team.delete()
            return redirect('/teams')
    return render(request, 'team/delete.html', context)


# to generate pdf---------------------------------------------

@login_required
def pdf_report_create(request, member_id):
    team = Team.objects.get(member_id=member_id)
    template_path = 'team/report.html'
    context = {'team': team}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Member_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

