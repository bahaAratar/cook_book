from django.shortcuts import render
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *


class AddProductToRecipe(APIView):
    @transaction.atomic
    def post(self, request, recipe_id, product_id, weight):
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)

        recipe_product = RecipeProduct.objects.filter(recipe=recipe, product=product).first()

        if recipe_product:
            recipe_product.weight = weight
            recipe_product.save()
            return Response('Вес обновлён')
        else:
            RecipeProduct.objects.create(recipe=recipe, product=product, weight=weight)
            return Response('Продукт успешно добавлен в рецепт')


class CookRecipe(APIView):
    @transaction.atomic
    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)

        for product in recipe.products.all():
            product.times_cooked += 1
            product.save()

        return Response('Рецепт успешно приготовлен')


class ShowRecipesWithoutProduct(APIView):
    @transaction.atomic
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        recipes = Recipe.objects.all()

        filtered_recipes = []

        for recipe in recipes:
            product_in_recipe = recipe.recipeproduct_set.filter(product=product).first()
            if not product_in_recipe or product_in_recipe.weight < 10:
                filtered_recipes.append(recipe)

        return render(request, 'recipes_without_product.html', {'recipes': filtered_recipes, 'product': product})
