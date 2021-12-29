from django.contrib import admin
from .models import Service, ServiceCategory

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'rating',
        'image',
    )

    ordering = ('name',)


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
