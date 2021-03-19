from django.contrib import admin
from .models import Category , Product,ShippingPrice
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug"]
    prepopulated_field = {"slug":("name",)}
admin.site.register(Category,CategoryAdmin) 


class ProductAdmin(admin.ModelAdmin):
    list_display=["name","price","stock","available","created","updated"]
    list_editable = ["price","stock","available"]
    prepopulated_field = {"slug":("name",)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

admin.site.register(ShippingPrice)

