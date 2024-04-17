from django.contrib import admin
from .my_models import Candle, Ingredient, Story, StoryType


class CandleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'story', 'ingredients')
    list_filter = ('ingredients', 'story')
    list_editable = ()
    search_fields = ('name', 'story', 'ingredients')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_filter = ()
    list_editable = ('name')
    search_fields = ('name')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('short_story_name', 'story_types')
    list_filter = ()
    list_editable = ('short_story_name', 'story_types')
    search_fields = ('short_story_name', 'story_types')


class StoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_filter = ()
    list_editable = ('name')
    search_fields = ('name')


# Register your models here.
admin.site.register(Candle.Candle)
admin.site.register(Ingredient.Ingredient)
admin.site.register(Story.Story)
admin.site.register(StoryType.StoryType)
