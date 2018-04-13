from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from event.forms import EventCreateForm

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