from django.contrib import admin
from .models import AssetHistory

class AssetHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('provide_date',)

admin.site.register(AssetHistory,AssetHistoryAdmin)
