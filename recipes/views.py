# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Recipe


def index(request):

    temp = """{"ingredients":{"wet ingredients":{"butter (unsalted)":{"amount":1,"unit":"cup"},"egg":{"amount":2,"unit":""},"white sugar":{"amount":0.66,"unit":"cup"},"brown sugar":{"amount":1,"unit":"cup"},"vanilla extract":{"amount":2,"unit":"teaspoon"}},"dry ingredients":{"all-purpose flour":{"amount":3,"unit":"cup"},"baking soda":{"amount":1,"unit":"teaspoon"},"salt":{"amount":1,"unit":"teaspoon"},"matcha powder":{"amount":2,"unit":"tablespoon"},"white chocolate chips":{"amount":1,"unit":"bag"}}},"recipe":{"duration":{"prep time":15,"cook time":15,"rest time":60},"directions":["Mix butter and sugars together until well mixed and smooth.","Add egg and vanilla extract and mix until well combined.","In a separate bowl, combine all dry ingredients. I advise to sift the matcha powder as it clumps easily.","Whisk dry ingredients together to mix everything evenly.","Slowly integrate dry ingredients with wet ingredients","Let rest covered in refrigerator for 60 min to overnight.","Bake at 350F for 15 minutes, rotating tray at the halfway mark."]}}"""
    recipe_list = Recipe.objects.order_by('pub_date')
    template = loader.get_template("recipes/index.html")
    context = {
        "recipe_list": recipe_list,
    }
    return HttpResponse(template.render(context, request))


def recipeView(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    temp_json = recipe.recipe
    steps = temp_json['recipe']['directions']
    ingredients = temp_json['ingredients']
    ing_array = [type for type in temp_json['ingredients']]
    name = "matcha white chocolate chip cookies"
    main_url = '/images/mwccc.jpg'

    template = loader.get_template("recipes/recipe.html")
    context = {
        "title": name,
        "main_url": main_url,
        "ingredients": ingredients,
        "ing_array": ing_array,
        "directions": steps,
    }
    return HttpResponse(template.render(context, request))
