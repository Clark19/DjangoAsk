from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelsAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['message']

    def short_desc(self, item):
        return item.desc[:20]
    short_desc.short_description = '아이템 간단 설명'