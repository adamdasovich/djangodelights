from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        menu = kwargs.pop('menu')
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['purchased_item'].queryset = MenuItem.objects.filter(pk__in=menu)


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'