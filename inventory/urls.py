from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('ingredient/', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/new/', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredient/<pk>/update', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredient/<pk>/delete', views.IngredientDelete.as_view(), name='ingredientdelete'),

    path('menu/', views.MenuList.as_view(), name='menulist'),
    path('menu/new/', views.MenuCreate.as_view(), name='menucreate'),
    path('menu/<pk>/update', views.MenuUpdate.as_view(), name='menuupdate'),
    path('menu/<pk>/delete', views.MenuDelete.as_view(), name='menudelete'),

    path('purchase/', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/<pk>/update', views.PurchaseUpdate.as_view(), name='purchaseupdate'),
    path('purchase/<pk>/delete', views.PurchaseDelete.as_view(), name='purchasedelete'),
    path('purchase/new/', views.PurchaseCreate.as_view(), name='purchasecreate'),

    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('recipes/new/', views.RecipeCreateView.as_view(), name='recipecreate'),
    path('recipes/<pk>/update', views.RecipeUpdateView.as_view(), name='recipeupdate'),
    path('recipes/<pk>/delete', views.RecipeDeleteView.as_view(), name='recipedelete'),
    

    path('reports/', views.ReportsView.as_view(), name='revenue_calc'),
]

