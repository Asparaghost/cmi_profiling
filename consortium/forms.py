from django import forms  
from consortium.models import CMI  


class CMIForm(forms.ModelForm):  

    class Meta:  
        model = CMI  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'agency_code': 'CMI Code',
            'name': 'Name',
            'is_cmi' : 'Is CMI',
            'address': 'Address',
            'geolat': 'Latitude',
            'geolong': 'Longitude',
            'contact_no': 'Contact Number',
            'logo': 'CMI Logo',
            'detail': 'Description',
            'telno': 'Telephone Number',
            'email': 'Email',
            'url': 'URL',
            'remarks': 'Remarks (Inactive)'
        }

