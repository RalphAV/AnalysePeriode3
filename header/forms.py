from django import forms
from .models import colorOutput, MessageText
import bleach

class nameForm(forms.ModelForm):

    name = forms.CharField()


    class Meta:
        model = colorOutput
        fields=(
                'name',
                'address',
        )

class colorForm(forms.ModelForm):

    class Meta:
        model = colorOutput
        fields=('color',
                )

class messageForm(forms.ModelForm):

    class Meta:
        model = MessageText
        fields  = (
            'text',
        )
    #
    # def clean_text(self):
    #     tags = ['b', 'a', 'i', 'strong']
    #     attributes = {'a': ['href']}
    #     text = self.cleaned_data['text']
    #     bleach.clean(text, tags=tags, attributes=attributes)
    #     return

