from django import template

register = template.Library()

# Mapping table
PERSIAN_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


@register.filter(name='persian_num')
def persian_numbers(value):
    """
    Convert all English digits in the value to Persian digits.
    Works with int, float, str, Decimal, etc.
    """
    if value is None:
        return ''

    # Convert to string first
    text = str(value)

    # Replace digits
    return text.translate(PERSIAN_DIGITS)