# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

STATUS_MAPPING = {
    '1': 'Pending',
    '2': 'Submitted to Vendor',
    '3': 'Completed',
}

@register.filter(name='status_display')
def status_display(value):
    return STATUS_MAPPING.get(str(value), value)