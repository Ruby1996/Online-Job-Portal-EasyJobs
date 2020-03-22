from django.contrib import admin

from .models import com_pro, Jobpost, interview, notification
# Register your models here.

admin.site.register(com_pro)

admin.site.register(Jobpost)

admin.site.register(interview)

admin.site.register(notification)



