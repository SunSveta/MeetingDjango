from django import template

register = template.Library()


@register.filter(is_safe=True)
def mediapath(text):
    return f'/media/{text}'


register = template.Library()


@register.simple_tag
def mediapath(text):
    return f'/media/{text}'
