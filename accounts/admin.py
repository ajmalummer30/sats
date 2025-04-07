from django.contrib import admin

from accounts.models import CustomUser, Department, Station



admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Station)


# Register your models here.
