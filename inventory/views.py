from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import IngredientForm
from django.urls import reverse

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
    template_name = 'inventory/ingredient_update.html'
    form_class = IngredientForm

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'

    def get_success_url(self):
        return reverse('ingredientlist')
    
