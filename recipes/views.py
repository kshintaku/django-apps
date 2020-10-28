# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Recipe
from .forms import SearchForm


def index(request, category=None):
    category_list = {}
    my_filter = {}
    form = SearchForm()
    category_view = False
    if category:
        my_filter["category"] = category
        category_list[category] = Recipe.objects.filter(**my_filter)
    elif request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            for cat in Recipe.CATEGORIES:
                my_filter["category"] = cat[0]
                results = set()
                recipe_list = Recipe.objects.filter(**my_filter)
                for recipe in recipe_list:
                    temp_json = recipe.recipe
                    ingredients = temp_json["ingredients"]
                    for list_type in ingredients:
                        for ingr in ingredients[list_type].keys():
                            if search_term in ingr:
                                results.add(recipe)
                category_list[cat[0]] = list(results)
            form = SearchForm()
        else:
            form = SearchForm()
    else:
        for cat in Recipe.CATEGORIES:
            my_filter["category"] = cat[0]
            category_list[cat[0]] = Recipe.objects.filter(**my_filter)[:1]
    template = loader.get_template("recipes/index.html")
    context = {
        "category_view": category_view,
        "category_list": category_list,
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


