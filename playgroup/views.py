from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from playgroup.forms import (PlayGroupForm,
                             MembershipFormset,
                             PlayGroupEventForm)
from playgroup.models import PlayGroup

from event.models import Event, Invitation


@login_required
def dashboard(request):
    owned_playgroups = PlayGroup.objects.filter(owner=request.user)
    return render(request, 'playgroup/dashboard.html', {
        'owned_playgroups': owned_playgroups,
    })


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = PlayGroupForm(request.POST)
        formset = MembershipFormset(request.POST)
    else:
        form = PlayGroupForm()
        formset = MembershipFormset()
    return render(request, 'playgroup/editor.html', {
        'form': form,
        'formset': formset,
    })


@login_required
def edit(request, group_id):
    playgroup = get_object_or_404(
        PlayGroup.objects.filter(owner=request.owner),
        id=playgroup_id)
    pass


@login_required
def details(request, group_id):
    playgroup = get_object_or_404(PlayGroup, pk=group_id)
    if not playgroup.viewable_by(request.user):
        raise Http404()
    events = playgroup.event_set.filter(date__gte=date.today()).order_by('date')
    return render(request, 'playgroup/details.html', {
        'playgroup': playgroup,
        'events': events,
    })


@login_required
@require_http_methods(["GET", "POST"])
def newevent(request, group_id):
    playgroup = get_object_or_404(
        PlayGroup.objects.filter(owner=request.user),
        id=group_id)
    if request.method == 'POST':
        form = PlayGroupEventForm(request.POST)
        if form.is_valid():
            event = Event(playgroup=playgroup,
                          name=form.cleaned_data['name'],
                          date=form.cleaned_data['date'])
            event.save()
            for member in playgroup.members.all():
                invitation = Invitation(event=event, member=member)
                invitation.save()
            return HttpResponseRedirect(playgroup.get_absolute_url())
    else:
        form = PlayGroupEventForm()

    return render(request, 'playgroup/newevent.html', {
        'playgroup': playgroup,
        'form': form,
    })
