from django import template

register = template.Library()

@register.filter(name='cut1')
def cut(value, arg):
    """
    This cuts out all values of "arg" from string!
    """

    return value.replace(arg, '')

#register.filter('cut', cut)
