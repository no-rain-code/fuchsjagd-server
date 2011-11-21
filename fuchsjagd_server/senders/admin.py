from django.contrib import admin

from senders.models import Sender, SenderGroup

class SenderInline(admin.TabularInline):
    model = Sender

class SenderGroupAdmin(admin.ModelAdmin):
    inlines = (SenderInline,)

admin.site.register(SenderGroup, SenderGroupAdmin)