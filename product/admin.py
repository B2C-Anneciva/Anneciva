from django.contrib import admin
from product.models import Category, Product, Comment, RatingStar, Rating

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(RatingStar)
admin.site.register(Rating)
