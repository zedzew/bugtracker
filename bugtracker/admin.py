from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('closed', 'title', 'text', 'created', 'user')
    list_filter = ['created', 'closed']
    search_field = ['title', 'text']

admin.site.register(Ticket, TicketAdmin)
