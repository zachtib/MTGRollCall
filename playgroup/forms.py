from django.forms import inlineformset_factory, ModelForm

from playgroup.models import PlayGroup, Membership


class PlayGroupForm(ModelForm):
    class Meta:
        model = PlayGroup
        exclude = ('owner', )


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        exclude = ()


MembershipFormset = inlineformset_factory(
    PlayGroup,
    Membership,
    form=MembershipForm)
