from flask import Flask, render_template, request, redirect, url_for
import recipe_magic as rm
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the homepage and handle form submission."""
    recipe = ""
    if request.method == 'POST':
        recipes = rm.load_recipes("recipes.json")
        recipe = rm.get_recipe_recommendation(recipes)
    return render_template('index.html', recipe=recipe)

@app.route('/rate_recipe', methods=['POST'])
def rate_recipe():
    scores = request.form.getlist('scores')
    scores = [int(score) for score in scores]  # Convert scores to integers
    recipe_id = request.form.get('recipe_id')  # Assuming each recipe has a unique ID
    rm.update_recipe_score(recipe_id, scores)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

