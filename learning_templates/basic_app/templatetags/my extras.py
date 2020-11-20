from django import template

register = template.Library()

@register.filter(name='cut') #pasa la funcion cut a la funcion filter
def cut(value,arg):
    """
    this cust out all values of arg from the string!
    """

    return value.replace(arg,'')

# register.filter('cut', cut)