from django.shortcuts import render
from .models import Category
from recipes.models import Recipe

def index(request):
    template ='foodie_app/index.html'
    categories = Category.objects.all()
    context ={'categories': categories}
    
    return render(request, template, context)

def recipes(request, category_id):
    template ='foodie_app/recipes.html'
    recipes = Recipe.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)
    context ={'recipes': recipes, 'category': category}
    
    return render(request, template, context)
