from django.contrib import admin

from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id","name","category","posted_on")
    search_fields = [ "name"]

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)