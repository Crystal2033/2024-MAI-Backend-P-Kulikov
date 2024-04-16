from django.db import models
from .Story import Story
from .Ingredient import Ingredient


class Candle(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default=None)
    ingredients = models.ManyToManyField(Ingredient, related_name="candles", default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
