from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredient/list/', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/new/', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('menu/list/', views.MenuList.as_view(), name='menulist'),
    path('menu/new/', views.MenuCreate.as_view(), name='menucreate'),
    path('menu/update/<pk>', views.MenuUpdate.as_view(), name='menuupdate'),
    path('menu/delete/<pk>', views.MenuDelete.as_view(), name='menudelete'),
    path('purchase/list/', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/update/<pk>', views.PurchaseUpdate.as_view(), name='purchaseupdate'),
    path('purchase/delete/<pk>', views.PurchaseDelete.as_view(), name='purchasedelete'),
    path('purchase/new/', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('finances/', views.finances, name='finances')
]

