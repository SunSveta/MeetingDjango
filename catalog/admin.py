from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category_id')
    search_fields = ('product_name', 'description')
    list_filter = ('category_id', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
