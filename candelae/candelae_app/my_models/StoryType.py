from django.db import models


# class StoryType:
#     def __init__(self, type_name):
#         self.type_name = type_name


class StoryType(models.Model):
    name = models.CharField(max_length=70, verbose_name="name")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
