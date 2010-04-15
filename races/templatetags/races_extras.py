from django import template

register = template.Library()

@register.filter(name="replace_char")
def replace_char(value, arg1, arg2):
    """
    Replaces a character with another
    """
    return value.replace(arg1, arg2)
    