from header.models import saveHeader
import re
import bleach

def headertype(a):
    if saveHeader.objects.all().filter(headerType=a).exists():
        object1 = saveHeader.objects.get(headerType=a)
        object1.amount += 1
        object1.save()
    else:
        object1 = saveHeader(headerType=a, amount=1)
        object1.save()

def createnameobject(name, address):
    return name, address


tags = ['b', 'a', 'i', 'strong']
attributes = {'a' : ['href']}

def cleanhtml(message):
    cleaned = bleach.clean(message, tags=tags, attributes=attributes)
    return cleaned
