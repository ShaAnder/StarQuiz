from django import template
import re

register = template.Library()

@register.filter(name='css_class')
def css_class(value):
    return re.sub(r'\s+', '-', value).lower()