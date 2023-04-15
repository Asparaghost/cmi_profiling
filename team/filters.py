import django_filters
from .models import Team

class TeamFilter(django_filters.FilterSet):
    fname = django_filters.CharFilter(lookup_expr='icontains', label="First Name")
    lname = django_filters.CharFilter(lookup_expr='icontains', label="Last Name")

    class Meta:
        model = Team
        fields = {'cmi': ['exact'],
                  'fname': ['icontains'],
                  'lname': ['icontains'],
        }

    def __init__(self, *args, **kwargs):
        super(TeamFilter, self).__init__(*args, **kwargs)
        self.filters['cmi'].label = 'CMI'
        self.filters['cmi'].extra['empty_label'] = "All"    
        


class TeamFilterDB(django_filters.FilterSet):
    position = django_filters.CharFilter(lookup_expr='icontains', label="Position")
    teams = django_filters.CharFilter(lookup_expr='icontains', label="Team")

    class Meta:
        model = Team
        fields = {'cmi': ['exact'],
                  'teams': ['icontains'],
                  'position': ['icontains'],
                  'sex': ['exact'],
        }

    def __init__(self, *args, **kwargs):
        super(TeamFilterDB, self).__init__(*args, **kwargs)
        self.filters['cmi'].label = 'CMI'
        self.filters['cmi'].extra['empty_label'] = "All"    
        self.filters['sex'].label = 'Sex'
        self.filters['sex'].extra['empty_label'] = "All" 
         