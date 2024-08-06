from django.db import models
from recipes.models import Recipe

# Create your models here.
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.comment