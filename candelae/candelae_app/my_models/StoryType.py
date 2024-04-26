from django.db import models


# class StoryType:
#     def __init__(self, type_name):
#         self.type_name = type_name


class StoryType(models.Model):
    name = models.CharField(max_length=70, verbose_name="Тип сюжета")

    class Meta:
        verbose_name = "Тип сюжета"
        verbose_name_plural = "Типы сюжетов"
        ordering = ["name"]
        db_table = "story_type"

    def __str__(self):
        return self.name

    def from_json_to_model(self):
        pass
