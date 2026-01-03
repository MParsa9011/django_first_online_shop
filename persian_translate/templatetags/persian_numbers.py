from django import template

register = template.Library()

@register.filter(name='persian_num')
def persian_numbers(value):
    """
    Convert all English digits in the value to Persian digits.
    Works with int, float, str, Decimal, etc.
    """
    if value is None:
        return ''

    # Convert to string first
    value = str(value)

    english_to_persian_table = value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

    # Replace digits
    return value.translate(english_to_persian_table)