# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Recipe
from .forms import SearchForm


def index(request):

    temp = """{"ingredients":{"wet ingredients":{"butter (unsalted)":{"amount":1,"unit":"cup"},"egg":{"amount":2,"unit":""},"white sugar":{"amount":0.66,"unit":"cup"},"brown sugar":{"amount":1,"unit":"cup"},"vanilla extract":{"amount":2,"unit":"teaspoon"}},"dry ingredients":{"all-purpose flour":{"amount":3,"unit":"cup"},"baking soda":{"amount":1,"unit":"teaspoon"},"salt":{"amount":1,"unit":"teaspoon"},"matcha powder":{"amount":2,"unit":"tablespoon"},"white chocolate chips":{"amount":1,"unit":"bag"}}},"recipe":{"duration":{"prep time":15,"cook time":15,"rest time":60},"directions":["Mix butter and sugars together until well mixed and smooth.","Add egg and vanilla extract and mix until well combined.","In a separate bowl, combine all dry ingredients. I advise to sift the matcha powder as it clumps easily.","Whisk dry ingredients together to mix everything evenly.","Slowly integrate dry ingredients with wet ingredients","Let rest covered in refrigerator for 60 min to overnight.","Bake at 350F for 15 minutes, rotating tray at the halfway mark."]}}"""
    category_list = {}
    form = SearchForm()
    recipe_list = Recipe.objects.order_by("pub_date")
    for cat in Recipe.CATEGORIES:
        my_filter = {}
        my_filter["category"] = cat[0]
        category_list[cat[0]] = Recipe.objects.filter(**my_filter)[:1]
    template = loader.get_template("recipes/index.html")
    context = {
        "category_list": category_list,
        "recipe_list": recipe_list,
        "form": form,
    }
    return HttpResponse(template.render(context, request))


def recipeView(request, recipe_id):
    form = SearchForm()
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    temp_json = recipe.recipe
    steps = temp_json["recipe"]["directions"]
    ingredients = temp_json["ingredients"]
    ing_array = [type for type in temp_json["ingredients"]]
    name = recipe.name
    main_url = recipe.img_url

    template = loader.get_template("recipes/recipe.html")
    context = {
        "title": name,
        "main_url": main_url,
        "ingredients": ingredients,
        "ing_array": ing_array,
        "directions": steps,
        "form": form,
    }
    return HttpResponse(template.render(context, request))


def categoryView(request, category):
    form = SearchForm()
    my_filter = {}
    my_filter["category"] = category
    recipe_list = Recipe.objects.filter(**my_filter)
    template = loader.get_template("recipes/category.html")
    context = {
        "category": category,
        "recipe_list": recipe_list,
        "form": form,
    }
    return HttpResponse(template.render(context, request))


def searchView(request):
    search_term = ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            form = SearchForm()
    else:
        form = SearchForm()
    results = set()
    recipe_list = Recipe.objects.order_by("pub_date")
    for recipe in recipe_list:
        temp_json = recipe.recipe
        ingredients = temp_json["ingredients"]
        for list_type in ingredients:
            for ingr in ingredients[list_type].keys():
                if search_term in ingr:
                    results.add(recipe)
    template = loader.get_template("recipes/search_results.html")
    print(results)
    context = {
        "recipe_list": results,
        "form": form,
    }
    return HttpResponse(template.render(context, request))