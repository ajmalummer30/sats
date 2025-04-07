from django.contrib import admin


from websockets.models import Counter, Ticket, Web_User_Profile



admin.site.register(Ticket)
admin.site.register(Counter)
admin.site.register(Web_User_Profile)
