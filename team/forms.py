from django import forms  
from .models import Team  


class TeamForm(forms.ModelForm):  
    date_appointed = forms.DateField(label='Date Appointed', required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['cmi'].empty_label = "Select CMI"
       

    class Meta:  
        model = Team  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'mname': 'Middle Name',
            'position': 'Position',
            'cmi': 'CMI',
            'teams': 'Team',
            'email_add': 'Email Address',
            'contact_no': 'Contact Number',
            'date_appointed': 'Date Appointed',
            #'dob': 'Date of Birth',
            'sex': 'Sex',
            # 'bach_deg': "Bachelor's Degree",
            # 'bdyearcompleted': "Bachelor's Degree Year Completed",
            # 'mas_deg': "Master's Degree",
            # 'mdyearcompleted': "Master's Degree Year Completed",
            # 'doc_deg': 'Doctorate Degree',
            # 'ddyearcompleted': 'Doctorate Degree Year Completed',
            'specialization': 'Specialization',
            'photo': 'Photo',
            'pds_file': 'Pds File',
        }

