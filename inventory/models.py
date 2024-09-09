from django.db import models
from datetime import datetime

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=15)
    unit_price = models.FloatField(default=0)

    def get_absolute_url(self):
        return '/ingredient/'
    
    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def get_absolute_url(self):
        return '/menu/'
    
    def __str__(self):
        return self.name + ' costs ' + str(self.price)
    
    def available(self):
        return all(n.enough() for n in self.reciperequirement_set.all())
    


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.quantity) + ' units of ' + self.ingredient.name + ' used in ' + self.menu_item.name
    
    def get_absolute_url(self):
        return '/recipes/'
    
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity


class Purchase(models.Model):
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    time_stamp = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.menu_item.name + ' purchased at ' + str(self.time_stamp)
    
    def get_absolute_url(self):
        return '/purchase/'
  