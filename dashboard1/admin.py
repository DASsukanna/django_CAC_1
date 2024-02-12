from django.contrib import admin

# Register your models here.
from .models import Club, Member, Event, Attendance

admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Attendance)

