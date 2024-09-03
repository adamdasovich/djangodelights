from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuForm, PurchaseForm
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
    model = MenuItem
    template_name = 'inventory/menu_delete.html'

    def get_success_url(self):
        return reverse('menulist')
    
##Purchase crud
##view to see store purchases
class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    form_class = PurchaseForm

##view to add a new purchase
class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_add.html'
    form_class = PurchaseForm

class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_update.html'
    form_class = PurchaseForm

class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_delete.html'

    def get_success_url(self):
        return reverse('menulist')



## view the profit and revenue
def finances(request):
    revenue = 0
    purchase = Purchase.objects.all()
    for item in purchase:
        revenue += item.menu_item.price
    context = {'revenue': revenue}
    return render(request, 'inventory/finance.html', context)













