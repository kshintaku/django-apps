from django.db import models


class RecipeManager(models.Manager):
    def create_recipe(self, title, recipe_json, pub_date_new):
        rec = self.create(name=title, recipe=recipe_json, pub_date=pub_date_new)
        return rec


class Recipe(models.Model):
    CATEGORIES = (
        ("breakfast", "BREAKFAST"),
        ("lunch", "LUNCH"),
        ("dinner", "DINNER"),
        ("dessert", "DESSERT"),
        ("drink", "DRINK"),
    )
    name = models.CharField("title", max_length=100)
    recipe = models.JSONField("Recipe")
    pub_date = models.DateTimeField("date published")
    img_url = models.CharField("image url", max_length=100)
    category = models.TextField("category", choices=CATEGORIES, default="dessert")
