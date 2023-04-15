from django.contrib import admin
from .models import Program, Researcher, Stakeholder, ProgramBudget

# Register your models here.
admin.site.register(Program)
admin.site.register(Researcher)
admin.site.register(Stakeholder)
admin.site.register(ProgramBudget)