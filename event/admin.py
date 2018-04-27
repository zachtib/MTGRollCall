from django.contrib import admin

from event.models import Event, Invitation


class InvitationInline(admin.TabularInline):
    model = Invitation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        InvitationInline,
    ]
    list_display = ('name', 'playgroup', 'date')
    date_hierarchy = 'date'


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('event', 'member', 'response', 'sent')
