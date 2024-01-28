from django.contrib import admin
from .models import Station, Train, Booking, Review

# Register your models here.
class StationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug']

admin.site.register(Train)
admin.site.register(Station,StationAdmin)
admin.site.register(Booking)
admin.site.register(Review)