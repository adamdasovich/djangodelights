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
]

