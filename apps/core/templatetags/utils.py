from django import template

register = template.Library()


@register.filter
def lookup(d, key):
    try:
        return d[int(key)-1]
    except IndexError:
        return None


@register.filter
def custom_range(number, arg=0):
    return range(arg, number)


@register.filter
def subtract(value, arg):
    return value - int(arg)
