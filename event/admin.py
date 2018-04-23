from django.contrib import admin

from event.models import Event, Invitation

class InvitationInline(admin.TabularInline):
    model = Invitation

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        InvitationInline,
    ]

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    pass