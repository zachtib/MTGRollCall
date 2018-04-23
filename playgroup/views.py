from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from playgroup.models import PlayGroup


@login_required
def dashboard(request):
    owned_playgroups = PlayGroup.objects.filter(owner=request.user)
    joined_playgroups = request.user.playgroups.all()
    return render(request, 'playgroup/dashboard.html', {
        'owned_playgroups': owned_playgroups,
        'joined_playgroups': joined_playgroups,
    })


@login_required
def create(request):
    pass


@login_required
def details(request, group_id):
    playgroup = get_object_or_404(PlayGroup, pk=group_id)
    if not playgroup.viewable_by(request.user):
        raise Http404()
    return render(request, 'playgroup/details.html', {
        'playgroup': playgroup,
    })