from django import template
from django.core.exceptions import FieldDoesNotExist

register = template.Library()

@register.filter
def get_verbose_name(reason, field_name):
    try:
        field = reason._meta.get_field(field_name)
        verbose_name = field.verbose_name

        if getattr(reason, field_name):
            return verbose_name

        return ""
    except (AttributeError, FieldDoesNotExist):
        return ""
    
@register.filter
def has_true_value(reasons, field_name):
    return reasons.filter(**{field_name: True}).exists()
