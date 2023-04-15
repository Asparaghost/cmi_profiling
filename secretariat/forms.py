from django import forms  
from .models import Secretariat 

class SecretariatForm(forms.ModelForm):  
    dob = forms.DateField(label='Date of Birth',required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))
    
    date_appointed = forms.DateField(label='Date Appointed',required=False, widget=forms.TextInput(     
        attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(SecretariatForm, self).__init__(*args, **kwargs)
        self.fields['consortium_id'].empty_label = "Select Consortium"
       

    class Meta:  
        model = Secretariat  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'mname': 'Middle Name',
            'position': 'Position',
            'consortium_id': 'Consortium',
            'email_add': 'Email Address',
            'contact_no': 'Contact Number',
            'date_appointed': 'Date Appointed',
            'dob': 'Date of Birth',
            'sex': 'Sex',
            'bach_deg': "Bachelor's Degree",
            'bdyearcompleted': "Bachelor's Degree Year Completed",
            'mas_deg': "Master's Degree",
            'mdyearcompleted': "Master's Degree Year Completed",
            'doc_deg': 'Doctorate Degree',
            'ddyearcompleted': 'Doctorate Degree Year Completed',
            'specialization': 'Specialization',
            'photo': 'Photo',
            'pds_file': 'Pds File',
        }

