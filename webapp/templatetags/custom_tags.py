from django import template
from random import randint


register = template.Library()

@register.simple_tag
def random_number():
    return randint(0,999)

@register.filter
def multiply(value, arg):
    return value * arg
