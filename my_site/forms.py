from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name:'), max_length=100)
    email = forms.EmailField(label='Email:')
    arrival_date = forms.DateField(label=_('Date of arrival:'), widget=forms.SelectDateWidget())
    party_size = forms.IntegerField(label=_('Party size:'))
    reference = forms.CharField(label=_('How did you find us?'), max_length=100)
    experiences = forms.CharField(label=_('What Experiences are you interested in?'),
                                  max_length=1000, widget=forms.Textarea)

