from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipes(request):
    recipes = Recipe.objects.all()
    template = 'recipes/recipes.html'
    context ={'recipes': recipes}
    return render(request, template, context)

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    tempate = 'recipes/recipe.html'
    context ={'recipe': recipe}
    return render(request, tempate, context)