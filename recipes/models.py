from django.db import models


class RecipeManager(models.Manager):
    def create_recipe(self, title, recipe_json, pub_date_new):
        rec = self.create(name=title, recipe=recipe_json, pub_date=pub_date_new)
        return rec


class Recipe(models.Model):
    name = models.CharField("title", max_length=100)
    recipe = models.JSONField("Recipe")
    pub_date = models.DateTimeField("date published")
    objects = RecipeManager()
