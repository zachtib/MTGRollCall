from event.templatetags import register
from event.models import Invitation


@register.filter(name='bg_class')
def bg_class(value):
    if value == Invitation.RESPONSE_YES_DISPLAY:
        return 'bg-success'
    elif value == Invitation.RESPONSE_NO_DISPLAY:
        return 'bg-danger'
    elif value == Invitation.NOT_RESPONDED_DISPLAY:
        return 'bg-warning'
    else:
        return 'bg-info'
