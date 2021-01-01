from django import template
#register all of this
register=template.Library()

#custom filter

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all values of args from string.txt
    """
    return value.replace(arg,'')

#register.filter('name_of_filter',cut) OR we can use decorators
