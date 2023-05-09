from django import forms  
from django.forms import ModelForm
from commodity.models import Commodity, IecMaterial

class CommodityForm(forms.ModelForm):  

    def __init__(self, *args, **kwargs):
        super(CommodityForm, self).__init__(*args, **kwargs)
        self.fields['cmi_name'].empty_label = "Select CMI"
        self.fields['stakeholder'].help_text = '<small style="color:green">Hold down “Control”, or “Command” on a Mac, to select more than one</small>'
    
    class Meta:  
        model = Commodity  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'name': 'Commodity Name',
            'detail': 'Details',
            'produced_by': 'Produced By',
            'cmi_name': 'CMI',
            'iec_id': 'Iec ID',
            'geolat': 'Latitude',
            'geolong': 'Longitude',
            'img': 'Image',
            'stakeholder': 'Commodity Adoptors',
        }
        



class IecMaterialForm(forms.ModelForm):  
    date_published = forms.DateField(label='Date Published', widget=forms.TextInput(     
        attrs={'type': 'date'}))


    def __init__(self, *args, **kwargs):
            super(IecMaterialForm, self).__init__(*args, **kwargs)
            self.fields['commodity'].empty_label = "None"

    class Meta:  
        model = IecMaterial  
        exclude = ('created_by', 'modified_by')
        fields = '__all__'
        labels = {
            'iec_type': 'IEC Type',
            'title': 'Title',
            'target_audience': 'Target Audience',
            'designed_by': 'Designed By',
            'content_by': 'Content By',
            'date_published': 'Date Published',
            'ip': 'IP',
            'iec_file': 'IEC File',
        }