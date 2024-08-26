from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('image', 'get_preview', 'number')

    def get_prevview(self, obj):
        return mark_safe('<img src="{url}" height=200 />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
