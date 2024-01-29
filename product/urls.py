from django.urls import path
from .views import *

urlpatterns = [
    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/', AddProductToRecipe.as_view()),
    path('cook_recipe/<int:recipe_id>/', CookRecipe.as_view()),
    path('show_recipes_without_product/<int:product_id>/', ShowRecipesWithoutProduct.as_view()),
]
