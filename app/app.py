from flask import Flask, render_template, request
import recipe_magic as rm
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the homepage and handle form submission."""
    recipe = ""
    if request.method == 'POST':
        recipe = rm.get_recipe_recommendation()
    return render_template('index.html', recipe=recipe)



if __name__ == '__main__':
    app.run(debug=True)

