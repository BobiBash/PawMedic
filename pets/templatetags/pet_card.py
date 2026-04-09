from django import template

register = template.Library()

@register.inclusion_tag('tags/pet_card.html')
def pet_card(pet):
    return {'pet': pet}