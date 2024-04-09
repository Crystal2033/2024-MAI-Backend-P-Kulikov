from django.db import models

from . import Story, Ingredient


# class Candle:
#     def __init__(self, uid, name, story_uid):
#         self.id = uid
#         self.name = name
#         self.story_id = story_uid


class Candle(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
