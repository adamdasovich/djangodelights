from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=15)
    unit_price = models.FloatField()


class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()



class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateField()
