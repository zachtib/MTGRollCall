from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

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