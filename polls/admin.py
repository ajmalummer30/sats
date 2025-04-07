from django.contrib import admin

from polls.models import *



admin.site.register(GeneralQuestion) 
admin.site.register(EquipmentSpecificQuestion)
admin.site.register(ChecklistDetails)
admin.site.register(Fuel)
admin.site.register(NatureOfInjury)
admin.site.register(Contractor)
admin.site.register(Workers)
admin.site.register(Fa_Category)
admin.site.register(Fa_SubCategory)
admin.site.register(Fa_Contract)
admin.site.register(Fa_ContractFile)
admin.site.register(Workpermit)
admin.site.register(CorrectiveMaintenance)
admin.site.register(PreventiveMaintenance)
admin.site.register(Workorder)