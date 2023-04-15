from django.conf import settings
from auditlog.registry import auditlog
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from auth_user.models import User
from consortium.models import CMI
from commodity.models import Commodity

# Create your models here.

class Researcher(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'

    CHOICE_SEX = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    researcher_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100, blank=True, null=True)
    cmi = models.ForeignKey(CMI, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=CHOICE_SEX, default=FEMALE)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='researcher_photo/', blank=True, null=True)
    pds_file = models.FileField(upload_to='researcher_pds/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="+", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lname) +", "+ (self.fname)
        
    class Meta:
        db_table = "researcher"

auditlog.register(Researcher)

class Program(models.Model):
    ONGOING = 'ongoing'
    COMPLETED = 'completed'

    CHOICE_STATUS = (
        (ONGOING, 'ongoing'),
        (COMPLETED, 'completed'),
    )

    prog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=CHOICE_STATUS, default=ONGOING)
    prog_description = models.TextField(blank=True, null=True)
    program_leader = models.ForeignKey(Researcher, related_name='+', on_delete=models.CASCADE)
    commodity = models.ManyToManyField(Commodity, blank=True, related_name="prog_com")
    impl_agency = models.ForeignKey(CMI, null=True, blank=True, related_name='programs', on_delete=models.CASCADE)
    co_impl_agency = models.ManyToManyField(CMI, blank=True)
    funding_agency = models.ForeignKey(CMI, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField()
    final_impl_date = models.DateField(blank=True, null=True)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    daterequestedext = models.DateField(blank=True, null=True)
    requested_by = models.ForeignKey(Researcher, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    ext_duration = models.IntegerField(blank=True, null=True)
    date_uploaded = models.DateField(blank=True, null=True)
    prog_file = models.FileField(upload_to='prog_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="+", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.prog_description[:130] + '...'


    class Meta:
        db_table = "program"

auditlog.register(Program, m2m_fields={"commodity", "co_impl_agency"})

class ProgramBudget(models.Model):
    progbdg_id = models.AutoField(primary_key=True)
    prog_id = models.ForeignKey(Program, related_name='prog_budg', on_delete=models.CASCADE)
    yr = models.IntegerField(blank=True, null=True)
    fund_source = models.ForeignKey(CMI, related_name='+', on_delete=models.CASCADE)
    ps = models.FloatField(blank=True, null=True)
    mooe = models.FloatField(blank=True, null=True)
    eo = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="+", blank=True, null=True, on_delete=models.CASCADE)

    
    class Meta:
        db_table = "program_budget"

auditlog.register(ProgramBudget)

class Stakeholder(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'

    CHOICE_SEX = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    stakeholder_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100, blank=True, null=True)
    cmi = models.ForeignKey(CMI, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    sex = models.CharField(max_length=10, choices=CHOICE_SEX, default=FEMALE)
    dob = models.DateField(blank=True, null=True)
    barangay = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)
    email_add = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="+", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (self.lname) +", "+ (self.fname)
        
    class Meta:
        db_table = "stakeholder"

auditlog.register(Stakeholder)
