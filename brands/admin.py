from django.contrib import admin
from brands.models import Brand


@admin.register(Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'description', 'created_at', 'updated_at')
    search_fields = ('brand_name',)
