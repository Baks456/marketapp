from django.contrib import admin
from django.utils.safestring import mark_safe

from goods.models import Categories, Products


# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'sort_level')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'category', 'description', 'show_image', 'image', ('price', 'discount'), 'quantity',)
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'price', 'discount', 'quantity',)
    list_editable = ('price', 'discount', 'quantity')
    readonly_fields = ('show_image',)
    search_fields = ('name', 'description')
    list_filter = ('category', 'quantity')

    @admin.display(description='Фото товара')
    def show_image(self, product: Products):
        if product.image:
            return mark_safe(f"<img src='{product.image.url}' width=300px>")
        return f'Нет фото'

# admin.site.register(Categories)
# admin.site.register(Products)
