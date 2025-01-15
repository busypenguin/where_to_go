from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminMixin

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ('image', 'get_preview', 'number')

    def get_preview(self, obj):
        return format_html(
                '<img src="{url}" style="max-height: {max_height}px; max-width: {max_width}px"/>',
                url=obj.image.url,
                max_height=200,
                max_width=300
                )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ('place',)
