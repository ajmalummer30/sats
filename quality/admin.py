from django.contrib import admin

from quality.models import Country, DriverInvolved, Employeesinvolved, In_BodyParts, In_Category, In_IncidentType, In_Incidents, In_NatureOfInjury, In_SurfaceCondition, In_Visibility, States, WhetherCondition



admin.site.register(In_IncidentType)
admin.site.register(WhetherCondition)
admin.site.register(In_Category)
admin.site.register(In_SurfaceCondition)
admin.site.register(In_NatureOfInjury)
admin.site.register(In_BodyParts)
admin.site.register(In_Visibility)
admin.site.register(In_Incidents)
admin.site.register(Employeesinvolved)
admin.site.register(DriverInvolved)
admin.site.register(Country)
admin.site.register(States)




