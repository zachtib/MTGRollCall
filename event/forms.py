from datetime import date
from django import forms


from playgroup.models import PlayGroup

class EventCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    playgroup = forms.ModelChoiceField(PlayGroup.objects.all())
    name = forms.CharField()
    date = forms.DateField()
    