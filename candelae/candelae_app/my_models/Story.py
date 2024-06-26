from django.db import models
from .StoryType import StoryType


class Story(models.Model):
    short_story_name = models.CharField(max_length=30, verbose_name="Сюжет", default="Краткое имя сюжета")
    description = models.TextField(verbose_name="Описание сюжета")
    story_types = models.ManyToManyField(StoryType, related_name="stories", default=None,
                                         verbose_name="Типы сюжета")

    class Meta:
        verbose_name = "Сюжет"
        verbose_name_plural = "Сюжеты"
        ordering = ["description"]
        db_table = "story"

    def __str__(self):
        return self.short_story_name

    def from_json_to_model(self):
        pass
