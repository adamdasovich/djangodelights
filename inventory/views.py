from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import IngredientForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_add.html'
    form_class = IngredientForm

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update'
    form_class = IngredientForm

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingridient_delete'
    form_class = IngredientForm
