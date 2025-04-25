from django.contrib import admin
from.models import *

# Register your models here.
admin.site.register(Server)
admin.site.register(UsageStats)
admin.site.register(Alerts)
admin.site.register(NetworkTraffic)