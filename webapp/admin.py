from django.contrib import admin

# Register your models here.
from .models import Category, Food, Rating

#admin.site.register(Category)
#admin.site.register(Food)

class adminCategorymodel(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,adminCategorymodel)

class adminFoodmodel(admin.ModelAdmin):
    list_display = ['foodname', 'available', 'price', 'description', 'image']
admin.site.register(Food,adminFoodmodel)

admin.site.register(Rating)