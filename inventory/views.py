from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import IngredientForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class ListIngredient(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients.html'

class CreateIngredient(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create.html'
    form_class = IngredientForm

class UpdateIngredient(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update'
    form_class = IngredientForm

class DeleteIngredient(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingridient_delete'
    form_class = IngredientForm
