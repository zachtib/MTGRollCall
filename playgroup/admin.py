from django.contrib import admin

from playgroup.models import PlayGroup, Membership


class MembershipInline(admin.TabularInline):
    model = Membership

@admin.register(PlayGroup)
class PlayGroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]