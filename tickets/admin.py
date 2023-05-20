from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Material)
admin.site.register(Refrigerant)
admin.site.register(Equipment)
admin.site.register(Reasons)
admin.site.register(Image)