from django.db import models
from django.contrib.auth .models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    fats = models.FloatField()
    proteins = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.name


class Consumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        # .name is a string ("Apple"), so this works perfectly!
        return self.food_consumed.name
