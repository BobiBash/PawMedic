from django import template

register = template.Library()

@register.inclusion_tag('tags/vet_card.html')
def vet_card(vet):
    return {'vet': vet}