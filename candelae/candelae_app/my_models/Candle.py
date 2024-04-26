from django.db import models
from .Story import Story
from .Ingredient import Ingredient


class Candle(models.Model):
    name = models.CharField(max_length=70, verbose_name="Название свечи")
    description = models.TextField(verbose_name="Описание свечи")
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default=None, verbose_name="Сюжет")
    ingredients = models.ManyToManyField(Ingredient, related_name="candles", default=None, verbose_name="Ингредиенты")

    class Meta:
        verbose_name = "Свеча"
        verbose_name_plural = "Свечи"
        ordering = ["name"]
        db_table = "candle"

    def __str__(self):
        return self.name


    def from_json_to_model(self):
        pass
