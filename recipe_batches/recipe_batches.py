#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  limiting_factor = None
  for item in recipe:
    if(item not in ingredients):
      return 0
    elif (limiting_factor == None or math.floor(ingredients[item] / recipe[item]) < limiting_factor):
      limiting_factor = math.floor(ingredients[item] / recipe[item])
  return limiting_factor

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

  # 1. 

  # I need to compare the recipe to ingredients to see how many of something I can make.

  # 2.

  # Easiest solution to this will be to divide each recipe by the related ingredients and round down (since I can't make 0.2 of a recipe).
  # I can track a minimum number and just replace as I iterate through the dicts.