from django.db import models

# Create your models here.
class saveHeader(models.Model):
    headerType = models.CharField(primary_key=True, max_length=100000)
    amount = models.IntegerField()

class colorOutput(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    address = models.CharField(max_length=100)

    COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
    color = models.CharField(choices=COLOR_CHOICES, default='green', max_length=10)

class MessageText(models.Model):
    text = models.TextField(max_length=100000)
