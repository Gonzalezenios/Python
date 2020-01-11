from django.contrib import admin
from.models import Comanda 

# Register your models here.
class ComandaAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Comanda, ComandaAdmin)

