from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from event.forms import EventCreateForm
from event.models import Event, Invitation


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            playgroup = form.cleaned_data['playgroup']
            event = Event(playgroup=playgroup, name=form.cleaned_data['name'], date=form.cleaned_data['date'])
            event.save()
            for member in playgroup.members.all():
                invitation = Invitation(event=event, member=member)
                invitation.save()
                invitation.send_email()
            return HttpResponseRedirect(reverse('event:thanks'))
    else:
        form = EventCreateForm()
    return render(request, 'event/create.html', {
        'form': form,
    })


@login_required
def details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if not event.viewable_by(request.user):
        raise Http404()

    response_dict = {
        Invitation.RESPONSE_YES_DISPLAY: {
            'count': 0,
            'percentage': '',
            'names': [],
        },
        Invitation.RESPONSE_NO_DISPLAY: {
            'count': 0,
            'percentage': '',
            'names': [],
        },
        Invitation.NOT_RESPONDED_DISPLAY: {
            'count': 0,
            'percentage': '',
            'names': [],
        },
    }

    invitations = event.invitations.select_related('member')

    for invite in invitations:
        response = invite.get_response_display()
        response_dict[response]['names'].append(invite.member.display_name)
    count = invitations.count()
    for key in response_dict.keys():
        response_dict[key]['count'] = len(response_dict[key]['names'])
        response_dict[key]['percentage'] = int(
            100 * response_dict[key]['count'] / count
        )

    return render(request, 'event/details.html', {
        'event': event,
        'responses': response_dict,
        'total_responses': count,
    })


def invitation(request, event_id, invite_id):
    invite = get_object_or_404(Invitation, id=invite_id, event__id=event_id)

    return render(request, 'email/invite.html', {
        'invitation': invite,
        'yes_url': reverse('event:respond', kwargs={
            'event_id': event_id,
            'invite_id': invite_id,
            'response': Invitation.RESPONSE_YES.lower()
        }),
        'no_url': reverse('event:respond', kwargs={
            'event_id': event_id,
            'invite_id': invite_id,
            'response': Invitation.RESPONSE_NO.lower()
        }),
    })


def respond(request, event_id, invite_id, response):
    invite = get_object_or_404(Invitation, id=invite_id, event__id=event_id)
    response = response.upper()
    if response not in (Invitation.RESPONSE_YES, Invitation.RESPONSE_NO):
        raise Http404()
    invite.response = response
    invite.save()
    return HttpResponseRedirect(reverse('event:thanks'))


def thanks(request):
    return render(request, 'event/thanks.html')
