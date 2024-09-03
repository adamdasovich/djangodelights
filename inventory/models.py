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
    
    def __str__(self):
        return self.name + ' costs ' + str(self.price)
    


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.quantity) + ' units of ' + self.ingredient.name + ' used in ' + self.menu_item.name
    
    ## function to calculate revenue
    def calcRev(self):
        revenue = self.menu_item.price - (self.ingredient.quantity * self.ingredient.price)
        return revenue


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateField()

    def __str__(self):
        return self.menu_item.name + ' purchased at ' + str(self.time_stamp)
    
    def get_absolute_url(self):
        return '/purchase/list'
