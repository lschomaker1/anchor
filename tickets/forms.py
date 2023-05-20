from django import forms
from .models import Ticket, Reasons, Equipment, Refrigerant, Material, Image
from jsignature.widgets import JSignatureWidget
from multiupload.fields import MultiFileField

class ReasonsForm(forms.ModelForm):

    class Meta:
        model = Reasons
        fields = ['pm', 'emer', 'warr', 'start', 'narep', 'inst', 'other']
        labels = {
            'pm': 'Preventative Maintenance',
            'emer': 'Emergency',
            'warr': 'Warranty',
            'start': 'Start-up',
            'narep': 'Non-Agreement Repair',
            'inst': 'Installation',
            'other': 'Other',
        }
        widgets = {
            'pm': forms.CheckboxInput(),
            'emer': forms.CheckboxInput(),
            'warr': forms.CheckboxInput(),
            'start': forms.CheckboxInput(),
            'narep': forms.CheckboxInput(),
            'inst': forms.CheckboxInput(),
            'other': forms.CheckboxInput(),
        }

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ['qty', 'desc', 'po', 'stock']
        exclude = ['delete']

class RefrigerantForm(forms.ModelForm):

    class Meta:
        model = Refrigerant
        fields = [
            'unit',
            'type',
            'qty',
            'tracking',
            'new',
            'recover',
            'recycle',
            'reclaim',
            'rc_ctr',
            'po'
        ]
        exclude = ['delete']

class ImageForm(forms.ModelForm):
    images = MultiFileField(min_num=0, max_num=10)

    class Meta:
        model = Image
        fields = ['images']

    def save_images(self, ticket):
        images = self.cleaned_data.get('images')
        for image in images:
            Image.objects.create(ticket=ticket, image=image)

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['recovery', 'torch', 'vacuum', 'power', 'tube', 'rig', 'special', 'other']
        labels = {
            'recovery': 'Recovery Machine',
            'torch': 'Torch/Welding Supplies',
            'vacuum': 'Vacuum Pump',
            'power': 'Power Washer',
            'tube': 'Tube Cleaner',
            'rig': 'Rigging Equipment',
            'special': 'Special Cleaning/Pumping Equip.',
            'other': 'Other',
        }
        widgets = {
            'recovery': forms.CheckboxInput(),
            'torch': forms.CheckboxInput(),
            'vacuum': forms.CheckboxInput(),
            'power': forms.CheckboxInput(),
            'tube': forms.CheckboxInput(),
            'rig': forms.CheckboxInput(),
            'special': forms.CheckboxInput(),
            'other': forms.CheckboxInput(),
        }

class TicketForm(forms.ModelForm):
    recovery = forms.BooleanField(required=False)
    torch = forms.BooleanField(required=False)
    vacuum = forms.BooleanField(required=False)
    power = forms.BooleanField(required=False)
    tube = forms.BooleanField(required=False)
    rig = forms.BooleanField(required=False)
    special = forms.BooleanField(required=False)
    other = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        cust_signature = cleaned_data.get('cust_signature')
        tech_signature = cleaned_data.get('tech_signature')

        # Check if cust_signature is empty and set it to None
        if not cust_signature:
            cleaned_data['cust_signature'] = None

        # Check if tech_signature is empty and set it to None
        if not tech_signature:
            cleaned_data['tech_signature'] = None

        return cleaned_data

    class Meta:
        model = Ticket
        fields = [
            'jobno',
            'jobname',
            'address',
            'city',
            'state',
            'zip',
            'auth_by',
            'report_to',
            'man1',
            'man2',
            'man3',
            'model1',
            'model2',
            'model3',
            'serial1',
            'serial2',
            'serial3',
            'unit1',
            'unit2',
            'unit3',
            'loc1',
            'loc2',
            'loc3',
            'desc',
            'day',
            'hours',
            'comments',
            'complete',
            'other',
            'week',
            'cust_signature',
            'tech_signature',
            ]
        widgets = {
            'cust_signature': JSignatureWidget(),
            'tech_signature': JSignatureWidget(),
        }
        exclude = ['user']