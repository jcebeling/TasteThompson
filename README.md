

## The Recipe Object

Every recipe object is structured in json form the same. Here is an example.

"name": "Test",
"prep_time": 60,
"ingredients": [
    {
        "name": "Test1",
        "unit": "lbs",
        "quantity": 2
    },
],
"instrucutions" : [
    "step 1 is to...",
    "step 2 is to..."
]
"score": 8,
"tags": [
    "chicken",
    "dinner",
    "rice"
],

We explain each of these fields below.

### Name
This is simply the name of the dish.

### Prep Time
This is the number of minutes it takes to prepare the dish.

### Ingredients
This is structured as a list of dictionaries, with each ingredient having the following attributes: name, unit, quantity.

### Instructions
These are the instructions for how to make the dish. This is structured as a list of strings.

### Score
This is a score out of 10 of how well like the dish is. This will need to get more complicated in future versions.

### Tags
This is a list of any keywords associated with the recipe.