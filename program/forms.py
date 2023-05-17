from django import forms  
from .models import Program, Researcher, Stakeholder, ProgramBudget 
from consortium.models import CMI
from commodity.models import Commodity  
from django.forms.widgets import Widget, CheckboxInput


class ProgramForm(forms.ModelForm):  
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    final_impl_date = forms.DateField(label='Final Implementation Date', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    daterequestedext = forms.DateField(label='Date Requested Extension', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    date_uploaded = forms.DateField(label='Date Uploaded', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    # co_impl_agency = forms.ModelMultipleChoiceField(label='Co-Implementing Agency(s)', required=False,
    #         queryset=Consortium.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
            
    # commodity = forms.ModelMultipleChoiceField(label='Program Commodity(s)', required=False,
    #         queryset=Commodity.objects.all(),
    #         widget=forms.CheckboxSelectMultiple)
    
    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.fields['program_leader'].empty_label = "Select Leader"
        self.fields['impl_agency'].empty_label = "None"
        self.fields['funding_agency'].empty_label = "None"
        self.fields['requested_by'].empty_label = "None"
        self.fields['requested_by'].empty_label = "None"
        self.fields['commodity'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
        self.fields['co_impl_agency'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
                  
    class Meta:  
        model = Program  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'title': 'Title',
            'prog_description': 'Description',
            'commodity': 'Program Commodity(s)',
            'program_leader': 'Program Leader',
            'impl_agency': 'Implementing Agency',
            'co_impl_agency': 'Co-Implementing Agency(s)',
            'funding_agency': 'Funding Agency',
            'start_date': 'Start Date',
            'duration': 'Duration',
            'ext_duration': 'Extension Duration',
            'final_impl_date': 'Final Implementation Date',
            'total_budget': 'Total Budget',
            'daterequestedext': 'Date Requested Extension',
            'requested_by': 'Requested By',
            'date_uploaded': 'Date Uploaded',
            'status': 'Status',
            'prog_file': 'Program File',
        }


class ResearcherForm(forms.ModelForm):  
    dob = forms.DateField(label='Date of Birth', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(ResearcherForm, self).__init__(*args, **kwargs)
        self.fields['cmi'].empty_label = "None"

    class Meta:  
        model = Researcher  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'mname': 'Middle Name',
            'cmi': 'CMI',
            'address': 'Address',
            'email': 'Email',
            'contact_no': 'Contact Number',
            'dob': 'Date of Birth',
            'sex': 'Sex',
            'specialization': 'Specialization',
            'photo': 'Photo',
            'pds_file': 'Pds File',
        }


class StakeholderForm(forms.ModelForm):  
    dob = forms.DateField(label='Date of Birth', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(StakeholderForm, self).__init__(*args, **kwargs)
        self.fields['consortium_id'].empty_label = "None"
        self.fields['commodity'].empty_label = "None"  

    class Meta:  
          model = Stakeholder  
          exclude = ('created_by', 'modified_by')
          fields = '__all__'
          labels = {
              'fname': 'First Name',
              'lname': 'Last Name',
              'mname': 'Middle Name',
              'sex': 'Sex',
              'dob': 'Date of Birth',
              'consortium_id': 'Consortium',
              'barangay': 'Barangay',
              'city': 'City',
              'province': 'Province',
              'zipcode': 'Zipcode',
              'email_add': 'Email Address',
              'contact_no': 'Contact Number',
              'commodity' : 'Adapted Commodity',
          }


class ProgramBudgetForm(forms.ModelForm):  

    def __init__(self, *args, **kwargs):
          super(ProgramBudgetForm, self).__init__(*args, **kwargs)
          self.fields['prog_id'].empty_label = "Select Program"
          self.fields['fund_source'].empty_label = "Select Agency"

    class Meta:  
          model = ProgramBudget  
          exclude = ('created_by', 'modified_by')
          fields = '__all__'
          labels = {
              'prog_id': 'Program',
              'yr': 'Year',
              'fund_source': 'Fund Source',
              'ps': 'PS',
              'mooe': 'MOOE',
              'eo': 'EO',
          }