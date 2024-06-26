from django.db import models


# class Ingredient:
#     def __init__(self, uid, name):
#         self.uid = uid
#         self.name = name

class Ingredient(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название ингредиента")

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ["name"]
        db_table = "ingredient"

    def __str__(self):
        return self.name

    def from_json_to_model(self, json_format):
        pass
