from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.forms import formset_factory
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, UpdateView
from jsignature.utils import draw_signature
from django.utils import timezone
from .models import Ticket, Equipment, Material, Refrigerant
from .forms import ReasonsForm, TicketForm, EquipmentForm, MaterialForm, RefrigerantForm
from io import BytesIO
from PIL import Image
import base64
from django.core.files.base import ContentFile
import re

class TicketList(ListView):
    model = Ticket
    context_object_name = 'tickets'


class TicketDetail(DetailView):
    model = Ticket
    fields = ['hours']
    context_object_name = 'ticket'
    template_name = 'tickets/ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ticket = self.object
        reasons = ticket.reasons

        if reasons:
            context['reasons'] = reasons
            

        field_names = ['pm', 'emer', 'warr', 'start', 'narep', 'inst', 'other']
        initial_data = {
            field_name: getattr(reasons, field_name, False)
            for field_name in field_names
        }
        form = ReasonsForm(initial=initial_data)

        # Update form rendering for checkboxes
        for field_name in field_names:
            field_value = getattr(reasons, field_name, False)
            form.fields[field_name].initial = field_value
            form.fields[field_name].widget.attrs['checked'] = field_value

        # Update form data to use boolean values instead of keys
        form.data = {key: str(getattr(self.object.reasons, key, False)) for key in form.initial}

        context['form'] = form
        context['equipment'] = ticket.equipment
        context['tech_signature_picture'] = self.request.session.get('tech_signature_picture') if ticket.tech_signature else None
        context['cust_signature_picture'] = self.request.session.get('cust_signature_picture') if ticket.cust_signature else None


        return context

def image_to_base64(image):
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_base64

def create_ticket(request):
    MaterialFormSet = formset_factory(MaterialForm, extra=1, can_delete=True)
    RefrigerantFormSet = formset_factory(RefrigerantForm, extra=1, can_delete=True)

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        reasons_form = ReasonsForm(request.POST)
        equipment_form = EquipmentForm(request.POST)
        material_formset = MaterialFormSet(request.POST, prefix='material')
        refrigerant_formset = RefrigerantFormSet(request.POST, prefix='refrigerant')
        if (ticket_form.is_valid() and
            reasons_form.is_valid() and
            equipment_form.is_valid() and
            material_formset.is_valid() and
            refrigerant_formset.is_valid()
            ):
            ticket = ticket_form.save(commit=False)  # Create a new Ticket instance without saving it
            reasons = reasons_form.save(commit=False)
            equipment = equipment_form.save(commit=False)
            cust_signature = ticket_form.cleaned_data.get('cust_signature')
            tech_signature = ticket_form.cleaned_data.get('tech_signature')

            material_instances = material_formset.save(commit=False)
            for material in material_instances:
                # Process each material instance
                
                # Set the ticket reference
                material.ticket = ticket
                material.save()
            
            refrigerant_instances = refrigerant_formset.save(commit=False)
            for refrigerant in refrigerant_instances:
                # Process each refrigerant instance
                
                # Set the ticket reference
                refrigerant.ticket = ticket
                refrigerant.save()


            if cust_signature:
                cust_signature_picture = draw_signature(cust_signature)
                cust_signature_picture_base64 = image_to_base64(cust_signature_picture)
                request.session['cust_signature_picture'] = cust_signature_picture_base64

            if tech_signature:
                tech_signature_picture = draw_signature(tech_signature)
                tech_signature_picture_base64 = image_to_base64(tech_signature_picture)
                request.session['tech_signature_picture'] = tech_signature_picture_base64


            reasons.ticket = ticket
            equipment.ticket = ticket
           
            
            # Assign boolean values from the form data
            reasons.pm = reasons_form.cleaned_data['pm']
            reasons.emer = reasons_form.cleaned_data['emer']
            reasons.warr = reasons_form.cleaned_data['warr']
            reasons.start = reasons_form.cleaned_data['start']
            reasons.narep = reasons_form.cleaned_data['narep']
            reasons.inst = reasons_form.cleaned_data['inst']
            reasons.other = reasons_form.cleaned_data['other']

            ticket.save()
            
            reasons_form.save()
            equipment.save()


            return redirect('ticket', pk=ticket.pk)  # Redirect to the detail view of the created ticket
    else:
        ticket_form = TicketForm()
        reasons_form = ReasonsForm()
        equipment_form = EquipmentForm()
        material_formset = MaterialFormSet(prefix='material')
        refrigerant_formset = RefrigerantFormSet(prefix='refrigerant')


    context = {
        'form': ticket_form,
        'reasons_form': reasons_form,
        'equipment_form': equipment_form,
        'tech_signature_picture': request.session.get('tech_signature_picture'),
        'cust_signature_picture': request.session.get('cust_signature_picture'),
        'material_formset': material_formset,
        'refrigerant_formset': refrigerant_formset,
    }

    return render(request, 'tickets/create_ticket.html', context)
