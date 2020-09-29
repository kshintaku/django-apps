from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json


def index(request):

    temp = """{"ingredients":{"wet ingredients":{"butter (unsalted)":{"amount":1,"unit":"cup"},"egg":{"amount":2,"unit":""},"white sugar":{"amount":0.66,"unit":"cup"},"brown sugar":{"amount":1,"unit":"cup"},"vanilla extract":{"amount":2,"unit":"teaspoon"}},"dry ingredients":{"all-purpose flour":{"amount":3,"unit":"cup"},"baking soda":{"amount":1,"unit":"teaspoon"},"salt":{"amount":1,"unit":"teaspoon"},"matcha powder":{"amount":2,"unit":"tablespoon"},"white chocolate chips":{"amount":1,"unit":"bag"}}},"recipe":{"duration":{"prep time":15,"cook time":15,"rest time":60},"directions":["mix butter and sugars together until well mixed and smooth.","add egg and vanilla extract and mix until well combined.","in a separate bowl, combine all dry ingredients. I advise to sift the matcha powder as it clumps easily","whisk dry ingredients together to mix everything evenly","slowly integrate dry ingredients with wet ingredients","let rest in refridgerator for 60 min to overnight","bake at 350F for 15 minutes, rotating tray at the halfway mark"]}}"""
    temp_json = json.loads(temp)
    steps = temp_json['recipe']['directions']
    ingredients = temp_json['ingredients']
    name = "matcha white chocolate chip cookies"

    template = loader.get_template("recipes/index.html")
    context = {
        "title": name,
        "ingredients": ingredients,
        "directions": steps,
    }
    return HttpResponse(template.render(context, request))
