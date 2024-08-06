from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe","comment", "date_added")
    search_fields = ["comment"]
# Register your models here.
admin.site.register(Comment, CommentAdmin)