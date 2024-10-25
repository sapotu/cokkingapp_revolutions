from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .logic import DISHES, ADULT, CHILDREN

from .models import  Recipe
def cooking_order(request):
    # {
    #     'dish':'upma',
    #     'adults':'20',
    #     'children':'10',
    # }
    #
    dish = request.POST.get("dish",'upma')
    total_adults = request.POST.get("adults",2)
    total_children = request.POST.get("children",1)
    if total_adults:
        total_adults = Recipe.objects.filter(dish=dish,is_adult=True).values()[0]
    if total_children:
        total_children = Recipe.objects.filter(dish=dish,is_adult=False).values()[0]

    initial_adult_qty = total_adults
    initial_children_qty = total_children

    final_adult_qty = {}
    final_children_qty = {}
    for key,value in total_adults.items():
        if key not in ['id','dish','is_adult'] and int(value) > 0:
            final_adult_qty[key] = value

    for key, value in total_children.items():
        if key not in ['id','dish','is_adult'] and int(value) > 0:
            final_children_qty[key] = value

    # final_adult_qty = {
    #     i: initial_adult_qty[i] * total_adults for i in initial_adult_qty
    # }
    # final_children_qty = {
    #     i: initial_children_qty[i] * total_children for i in initial_children_qty
    # }
    final_qty = {
        key: final_adult_qty[key] + final_children_qty[key] for key in final_children_qty
    }
    response = {dish: final_qty}
    return JsonResponse(response)
