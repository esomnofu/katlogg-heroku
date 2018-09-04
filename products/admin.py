from django.contrib import admin
from .models import Product, News, Ratings, Unidentified

admin.site.register(Ratings)
admin.site.register(Product)
admin.site.register(News)
admin.site.register(Unidentified)