from django.contrib import admin
from .models import Department, Equipment, Material, Requisition

admin.site.register(Department)
admin.site.register(Equipment)
admin.site.register(Material)
admin.site.register(Requisition)