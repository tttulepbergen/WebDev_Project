from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Category)
