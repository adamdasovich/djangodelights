from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.ListIngredient.as_view(), name='ingredients'),
    path('ingredients/new/', views.CreateIngredient.as_view(), name='create_ingredient'),
    path('ingredients/<pk>/update/', views.UpdateIngredient.as_view(), name='update_ingredient'),
    path('ingredients/<pk>/delete/', views.DeleteIngredient.as_view(), name='delete_ingredient'),
]

