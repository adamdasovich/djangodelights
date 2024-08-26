from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=15)
    unit_price = models.FloatField()

    def get_absolute_url(self):
        return '/ingredient/list'
    


class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def get_absolute_url(self):
        return '/menu/list'
    


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateField()
