import random
from django import template

register = template.Library()


@register.simple_tag
def random_thing():
    a = 1
    b = 10
    if b is None:
        a, b = 0, a
    return random.randint(a, b)
