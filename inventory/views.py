from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuForm
from django.urls import reverse

# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

## Ingredient CRUD

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
    

    
## Menu CRUD
class MenuList(ListView):
    model = MenuItem
    template_name = 'inventory/menu_list.html'

class MenuCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menu_add.html'
    form_class = MenuForm

class MenuUpdate(UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_update.html'
    form_class = MenuForm

class MenuDelete(DeleteView):
    model = MenuForm
    template_name = 'inventory/menu_delete.html'

    def get_success_url(self):
        return reverse('menulist')
    
