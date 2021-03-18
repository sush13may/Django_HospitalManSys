from django.contrib import admin
from .models import PatientUser, StaffUser


# Register your models here.
class PatientUserAdmin(admin.ModelAdmin):
     fields = ('reg_user', 'gender')
     list_display = ('reg_user', 'gender')


class StaffUserAdmin(admin.ModelAdmin):
    fields = ('reg_user', 'job')
    list_display = ('reg_user', 'job')


admin.site.register(PatientUser, PatientUserAdmin)
admin.site.register(StaffUser, StaffUserAdmin)
