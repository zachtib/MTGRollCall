from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render

import os

def autoconfigure(request):
    users = User.objects.all()
    if users.count() != 0:
        raise Http404()

    username = os.environ.get('ADMIN_USERNAME')
    email = os.environ.get('ADMIN_EMAIL')
    password = os.environ.get('ADMIN_PASSWORD')
    if not username or not password:
        raise Http404()

    admin = User(username=username, email=email)
    admin.set_password(password)
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()

    return HttpResponse('Admin user created')


def dashboard(request):
    return render(request, 'base.html')