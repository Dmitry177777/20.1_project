from django.contrib import admin

from main.models import Product, Category

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description','product_category',  )
    search_fields = ('product_name', 'description',)
    list_filter = ('is_active', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category', 'description', )
    search_fields = ('product_category', 'description',)
    list_filter = ('is_active', )