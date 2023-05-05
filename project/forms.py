from django import forms  
from consortium.models import CMI
from commodity.models import Commodity
from program.models import Researcher, Stakeholder
from .models import Sdg, Project, PriorityArea, ProjectOutput, ProjectImplementingSite


class SdgForm(forms.ModelForm):  

    class Meta:  
        model = Sdg  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'sdg_title': 'Title',
            'sdg_desc': 'Description',
        }


class ProjectForm(forms.ModelForm):  
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    end_date = forms.DateField(label='End Date', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    approved_date = forms.DateField(label='Approved Date', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    daterequestedext = forms.DateField(label='Date Requested Extension', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    date_uploaded = forms.DateField(label='Date Uploaded', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    final_impl_date = forms.DateField(label='Final Implementation Date', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    # commodity = forms.ModelMultipleChoiceField(label='Commodity(s)', required=False,
    #         queryset=Commodity.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
    
    # proj_team = forms.ModelMultipleChoiceField(label='Project Team', required=False, 
    #         queryset=Researcher.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
    
    # proj_stakeholder = forms.ModelMultipleChoiceField(label='Project Stakeholder(s)', required=False,
    #         queryset=Stakeholder.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
    
    # co_impl_agency = forms.ModelMultipleChoiceField(label='Co-Implementing Agency(s)', 
    #         queryset=Consortium.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
    
    # coop_agency = forms.ModelMultipleChoiceField(label='Cooperating Agency(s)',
    #         queryset=Consortium.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['prog_id'].empty_label = "None"
        self.fields['proj_leader'].empty_label = "Select Leader"
        self.fields['priority'].empty_label = "None"
        self.fields['sdg_no'].empty_label = "None"
        self.fields['impl_agency'].empty_label = "Select Agency"
        self.fields['fund_agency'].empty_label = "Select Agency"
        self.fields['requested_by'].empty_label = "Select Person"
        self.fields['commodity'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
        self.fields['proj_team'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
        self.fields['proj_stakeholder'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
        self.fields['co_impl_agency'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
        self.fields['coop_agency'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
        

    class Meta:  
        model = Project  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'title': 'Title',
            'prog_id': 'Program',
            'proj_description': 'Project Description',
            'proj_type': 'Project Type',
            #'proj_type_sub': 'Title',
            'commodity': 'Commodity(s)',
            'proj_leader': 'Project Leader',
            'priority': 'Priority Area',
            'sdg_no': 'SDG',
            'proj_team': 'Project Team',
            'proj_stakeholder': 'Stakeholder(s)',
            'impl_agency': 'Implementing Agency',
            'co_impl_agency': 'Co-Implementing Agency(s)',
            'coop_agency': 'Cooperating Agency(s)',
            'fund_agency': 'Funding Agency',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'final_impl_date': 'Final Implementation Date',
            'duration': 'Duration',
            'approved_budget': 'Approved Budget',
            'approved_date': 'Approved Date',
            'daterequestedext': 'Date Requested Extension',
            'requested_by': 'Requested By',
            'ext_duration': 'Extension Duration',
            'proj_file': 'Project File',
            'date_uploaded': 'Date Uploaded',
            'status': 'Status',
        }


class PriorityAreaForm(forms.ModelForm):  

    class Meta:  
        model = PriorityArea  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'area': 'Area',
            'description': 'Description',
        }


class ProjectOutputForm(forms.ModelForm):  

    def __init__(self, *args, **kwargs):
              super(ProjectOutputForm, self).__init__(*args, **kwargs)
              self.fields['proj_id'].empty_label = "Select Project"
              self.fields['iec_id'].empty_label = "None"


    class Meta:  
        model = ProjectOutput 
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'proj_id': 'Project',
            'proj_output_type': 'Output Type',
            'proj_output_desc': 'Description',
            'iec_id': 'IEC Material',
        }


class ProjectImplementingSiteForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
            super(ProjectImplementingSiteForm, self).__init__(*args, **kwargs)
            self.fields['proj_id'].empty_label = "Select Project"

    class Meta:  
        model = ProjectImplementingSite
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'proj_id': 'Project',
            'barangay': 'Barangay',
            'city': 'City',
            'province': 'Province',
            'zipcode': 'Zipcode',
            'geolat': 'Latitude',
            'geolong': 'Longitude',
        }