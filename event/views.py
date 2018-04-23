from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from event.forms import EventCreateForm
from event.models import Invitation

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            playgroup = form.cleaned_data['playgroup']
            print(playgroup)

    else:
        form = EventCreateForm()
    return render(request, 'event/create.html', {
        'form': form,
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
