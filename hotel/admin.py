from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'HOTEL BOOKING SYSTEM'
admin.site.register(roomtype)
admin.site.register(room)


admin.site.register(reservation)

