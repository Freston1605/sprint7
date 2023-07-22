from django import template

register = template.Library()

@register.filter
def get_urgencia_color(urgencia):
    if urgencia == 'Alta':
        return 'table-danger'
    elif urgencia == 'Media':
        return 'table-warning'
    elif urgencia == 'Baja':
        return 'table-success'
    else:
        return ''