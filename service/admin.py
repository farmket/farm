from django.contrib import admin
from .models import Product,Category,Feedback,Shop,Item,SubCategory,Facility


admin.site.register(Item)
admin.site.register(Facility)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Feedback)
#admin.site.register(UserForm)

# Register your models here.
# class ProductInline(admin.TabularInline):
#     model = Product
#     raw_id_fields = ['name']

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','updated_at']
    list_filter = ['category', 'created_at', 'updated_at']
  #  inlines = [ProductInline]

admin.site.register(Shop,ShopAdmin)
