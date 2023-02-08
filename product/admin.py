from django.contrib import admin
from product.models import Category, Product, Comment, RatingStar, Rating


@admin.register(Product)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name', 'category')
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(RatingStar)
admin.site.register(Rating)
