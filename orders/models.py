from django.db import models

# Create your models here.
DISHES = ["upma", "dosa", "idly"]


ADULT = {
    "upma": {"flour": 100, "oil": 10, "salt": 1, "water": 200},
    "dosa": {"rice": 100, "oil": 10, "salt": 1, "water": 200},
    "idly": {"rice": 100, "oil": 10, "salt": 10},
}
CHILDREN = {
    "upma": {"flour": 100, "oil": 10, "salt": 1, "water": 200},
    "dosa": {"rice": 100, "oil": 5, "salt": 1, "water": 200},
    "idly": {"rice": 100, "oil": 7, "salt": 10},
}



# class Dish:
#     name = models.CharField(max_length=100)


class Recipe(models.Model):
    wheat = models.IntegerField(default=0)
    flour = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    salt = models.IntegerField(default=0)
    dish = models.CharField(max_length=32)
    is_adult = models.BooleanField(default=True)


# class Quantity:
#     quantity = models.IntegerField()
#
# class Order:
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
#     is_adult = models.BooleanField(default=True)
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     qty = models.ForeignKey(Quantity, on_delete=models.CASCADE)

# dish --> dish_id, ingredients_id, qty_id, is_adult


# dish, ingredients,