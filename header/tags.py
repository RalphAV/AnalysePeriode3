from django import template
from .models import colorOutput

register = template.Library()

@register.simple_tag()
def displayname(request):
    object = colorOutput.objects.latest('name')
    print(object)
