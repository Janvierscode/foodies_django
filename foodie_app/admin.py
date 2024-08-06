from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ["name"]
    list_filter = ["name"]
    
    
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "Category", "posted_on")
# Register your models here.
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Recipe, RecipeAdmin)