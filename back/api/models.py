from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)    
    category = models.CharField(max_length=100)  # Например: мясо, овощи, фрукты и т. д.
    image = models.ImageField(upload_to='ingredients', null=True, blank=True)
    def __str__(self):        
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=200)    
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')    
    instructions = models.TextField()
    categories = models.ManyToManyField('Category')    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class RecipeIngredient(models.Model):   
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)    
    quantity = models.CharField(max_length=50)

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()    
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Favorite(models.Model):    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:        
        unique_together = ('recipe', 'user')