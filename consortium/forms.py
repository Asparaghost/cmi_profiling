from django import forms  
from consortium.models import CMI, Consortium  


class CMIForm(forms.ModelForm):  

    def __init__(self, *args, **kwargs):
        super(CMIForm, self).__init__(*args, **kwargs)
        self.fields['consortium_id'].empty_label = "Select Consortium"

    class Meta:  
        model = CMI  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'agency_code': 'CMI Code',
            'name': 'Name',
            'is_cmi' : 'Is CMI',
            'consortium_id' : 'Consortium',
            'address': 'Address',
            'geolat': 'Latitude',
            'geolong': 'Longitude',
            'contact_no': 'Contact Number',
            'logo': 'CMI Logo',
            'detail': 'Description',
            'telno': 'Telephone Number',
            'email': 'Email',
            'url': 'URL',
            'status': 'Status',
            'remarks': 'Remarks (Inactive)'
        }


class ConsortiumForm(forms.ModelForm):  

    class Meta:  
        model = Consortium  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'consortium_name': 'Consortium Name',
            'consortium_code': 'Consortium Code',
            'consortium_address' : 'Address',
            'geolat': 'Latitude',
            'geolong': 'Longitude',
            'consortium_logo': 'Consortium Logo',
            'mission': 'Mission',
            'vision': 'Vision',
            'consortium_desc': 'Description',
            'consortium_objectives': 'Objectives',
            'url': 'URL',
            'fb_url': 'Facebook',
            'yt_url': 'Youtube',
            'telno': 'Telephone Number',
            'email': 'Email Address',
        }

