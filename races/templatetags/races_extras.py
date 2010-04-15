from django import template

register = template.Library()

@register.filter(name="replace_char")
def replace_char(value, arg):
    """
    Replaces a character with another char
    value = value to be filtered
    arg = string of len 2, first char to be replaced with second char 
    """
    return value.replace(arg[0], arg[1])
    