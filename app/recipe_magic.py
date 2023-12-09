import json
import random

def load_recipes(filename):
    """Load recipes from a JSON file."""
    with open(filename) as file:
        return json.load(file)

def get_recipe_recommendation(recipes):
    """Return a recommended recipe from the list."""
    return random.choice(recipes)

def update_recipe_score(recipe_id, new_scores):
    recipes = load_recipes('recipes.json')
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)

    if recipe:
        # Calculate the new average score
        total_scores = sum(new_scores)
        num_scores = len(new_scores)
        recipe['score'] = total_scores / num_scores

        # Update the JSON file
        with open('recipes.json', 'w') as file:
            json.dump(recipes, file)