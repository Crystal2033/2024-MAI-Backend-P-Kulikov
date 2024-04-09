from django.db import models


# class Ingredient:
#     def __init__(self, uid, name):
#         self.uid = uid
#         self.name = name

class Ingredient(models.Model):
    name = models.CharField(max_length=30)