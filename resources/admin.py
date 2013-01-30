from resources.models import Catalog, ResFile
from django.contrib import admin

class ResInline(admin.TabularInline):
    model = ResFile
    extra = 5

class CatalogAdmin(admin.ModelAdmin):
    field = ['name', 'desc']
    inlines = [ResInline]

admin.site.register(Catalog, CatalogAdmin)
