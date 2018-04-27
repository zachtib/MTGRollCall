from django import forms

from playgroup.models import PlayGroup, Membership
from event.models import Event


class PlayGroupForm(forms.ModelForm):
    class Meta:
        model = PlayGroup
        exclude = ('owner', )


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        exclude = ()


MembershipFormset = forms.inlineformset_factory(
    PlayGroup,
    Membership,
    form=MembershipForm)


class PlayGroupEventForm(forms.Form):
    name = forms.CharField()
    date = forms.DateField()
