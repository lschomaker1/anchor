from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from jsignature.fields import JSignatureField

# Create your models here.

class Ticket(models.Model):
    DAY = [
        ('M', 'MONDAY'),
        ('TU', 'TUESDAY'),
        ('W', 'WEDNESDAY'),
        ('TH', 'THURSDAY'),
        ('F', 'FRIDAY'),
        ('SA', 'SATURDAY'),
        ('SU', 'SUNDAY'),
    ]

    FIELD_VERBOSE_NAMES = {
        'pm': 'Preventative Maintenance',
        'emer': 'Emergency',
        'warr': 'Warranty',
        'start': 'Startup',
        'narep': 'Non-Agreement Repair',
        'inst': 'Installation',
        'other': 'Other',
    }


    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    week = models.DateField(null=True, blank=True)
    jobno = models.CharField(max_length=30, null=True, blank=True)
    jobname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length = 60, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    auth_by = models.CharField(max_length=30, null=True, blank=True)
    report_to = models.CharField(max_length=30, null=True, blank=True)
    man1 = models.CharField(max_length=70, null=True, blank=True)
    man2 = models.CharField(max_length=70, null=True, blank=True)
    man3 = models.CharField(max_length=70, null=True, blank=True)
    model1 = models.CharField(max_length=70, null=True, blank=True)
    model2 = models.CharField(max_length=70, null=True, blank=True)
    model3 = models.CharField(max_length=70, null=True, blank=True)
    serial1 = models.CharField(max_length=70, null=True, blank=True)
    serial2 = models.CharField(max_length=70, null=True, blank=True)
    serial3 = models.CharField(max_length=70, null=True, blank=True)
    unit1 = models.IntegerField(null=True, blank=True)
    unit2 = models.IntegerField(null=True, blank=True)
    unit3 = models.IntegerField(null=True, blank=True)
    loc1 = models.CharField(max_length=70, null=True, blank=True)
    loc2 = models.CharField(max_length=70, null=True, blank=True)
    loc3 = models.CharField(max_length=70, null=True, blank=True)
    desc = models.TextField(max_length=700, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    day = models.CharField(max_length=2, choices=DAY, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    comments = models.TextField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(null=True, blank=True)
    cust_signature = JSignatureField(blank=True, null=True)
    tech_signature = JSignatureField(blank=True, null=True)
    def __str__(self):
        return f"Ticket #{self.pk}"
    
class Image(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class Reasons(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=1, related_name='reasons')
    pm = models.BooleanField(verbose_name='Preventative Maintenance', default=False, null=True, blank=True)
    emer = models.BooleanField(verbose_name='Emergency', default=False, null=True, blank=True)
    warr = models.BooleanField(verbose_name='Warranty', default=False, null=True, blank=True)
    start = models.BooleanField(verbose_name='Startup', default=False, null=True, blank=True)
    narep = models.BooleanField(verbose_name='Non-Agreement Repair', default=False, null=True, blank=True)
    inst = models.BooleanField(verbose_name='Installation', default=False, null=True, blank=True)
    other = models.BooleanField(verbose_name='Other', default=False, null=True, blank=True)

    def get_verbose_name(self, field_name):
        field = self._meta.get_field(field_name)
        return field.verbose_name

class Material(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=1, related_name='material')
    qty = models.CharField(max_length=10, null=True, blank=True)
    desc = models.CharField(max_length=70, null=True, blank=True)
    po = models.CharField(max_length=40, null=True, blank=True)
    stock = models.CharField(max_length=70, null=True, blank=True)

class Refrigerant(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=1, related_name='refrigerant')
    unit = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    qty = models.CharField(max_length=25, null=True, blank=True)
    tracking = models.CharField(max_length=30, null=True, blank=True)
    new = models.BooleanField(null=True, blank=True)
    recover = models.BooleanField(null=True, blank=True)
    recycle = models.BooleanField(null=True, blank=True)
    reclaim = models.BooleanField(null=True, blank=True)
    rc_ctr = models.CharField(max_length=70, null=True, blank=True)
    po = models.CharField(max_length=30, null=True, blank=True)

class Equipment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="equipment", default=1)
    recovery = models.BooleanField(null=True, blank=True)
    torch = models.BooleanField(null=True, blank=True)
    vacuum = models.BooleanField(null=True, blank=True)
    power = models.BooleanField(null=True, blank=True)
    tube = models.BooleanField(null=True, blank=True)
    rig = models.BooleanField(null=True, blank=True)
    special = models.BooleanField(null=True, blank=True)
    other = models.BooleanField(null=True, blank=True)