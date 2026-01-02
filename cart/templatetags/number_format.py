from django import template

register = template.Library()

@register.filter
def comma_number(value):
    try:
        value = float(value)
    except:
        return value

    return f"{value:,.0f}"