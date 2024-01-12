from django import template

register=template.Library()
# @register.filter('swapping')# swapping is the filter name for swap function


def u(value):

    return value.upper()


def l(value):

    return value.lower()

def remove_h(data,value):

    strr = list(data)
    strr.remove(value)



    return ''.join(strr)

register.filter('u',u)

register.filter('l',l)
register.filter('remove_h',remove_h)
