from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuForm, PurchaseForm, RecipeRequirementForm
from django.db.models import Sum
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

##view to add a new purchase
class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_add.html'
    form_class = PurchaseForm

    def get_menu(self):
        return [m.pk for m in MenuItem.objects.all() if m.available()]

    def get_form_kwargs(self):
        kwargs = super(PurchaseCreate, self).get_form_kwargs()
        kwargs['menu'] = self.get_menu()
        print(self.get_menu())
        return kwargs
    
    def form_valid(self, form):
        purchased_item = form.cleaned_data['purchased_item']
        used_ingredients = purchased_item.reciperequirement_set.all()
        for i in used_ingredients:
            i.ingredient.quantity -= i.quantity
            i.ingredient.save()
        return super().form_valid(form)

class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_update.html'
    form_class = PurchaseForm

class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_delete.html'

    def get_success_url(self):
        return reverse('menulist')
    
## Recipe Crud
class RecipeView(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipes.html'

class RecipeCreateView(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_create.html'
    fields = ['menu_item', 'ingredient', 'quantity']
    #class_form = RecipeRequirementForm

class RecipeUpdateView(UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_update.html'
    class_form = RecipeRequirementForm

class RecipeDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_delete.html'



## view the profit and revenue
class ReportsView(TemplateView):
    template_name = 'inventory/finance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        context['purchases'] = purchases
        revenue = purchases.aggregate(revenue=Sum('purchased_item__price'))['revenue']
        context['total_revenue'] = round(revenue, 2)
        total_cost = 0
        for purchase in purchases:
            for ingred in purchase.purchased_item.reciperequirement_set.all():
                total_cost += (ingred.ingredient.unit_price * ingred.quantity)
        context["total_cost"] = round(total_cost, 2)
        context['profit'] = round((revenue - total_cost), 2) 
        return context
    












