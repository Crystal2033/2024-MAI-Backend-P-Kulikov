# class Story:
#     def __init__(self, uid, description):
#         self.uid = uid
#         self.desc = description

from django.db import models
from . import StoryType


# class Story(models.Model):
#     description = models.TextField()
#     story_types = models.ManyToManyField(StoryType, related_name="story_types")
