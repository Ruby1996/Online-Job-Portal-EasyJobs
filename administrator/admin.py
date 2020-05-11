from django.contrib import admin

from .models import helpdesk,reply,payments
# Register your models here.

admin.site.register(helpdesk)
admin.site.register(reply)
admin.site.register(payments)