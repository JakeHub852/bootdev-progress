def check_ingredient_match(recipe, ingredients):
    correct = 0
    missing = []
    for ingredient in recipe:
        if ingredient in ingredients:
            correct += 1
        else:
            missing.append(ingredient)
    percentage = correct / len(recipe) * 100
    return percentage, missing

"""
Let's break down the magic woven into that check_ingredient_match function. You've used a few fundamental concepts of programming:

1.Function Definition: The line def check_ingredient_match(recipe, ingredients): defines a function. A function is a reusable block of code that performs a specific task. 
In this case, its task is to compare two lists and figure out what's missing and the completion percentage. 
The things in the parentheses (recipe and ingredients) are called parameters – they are the values the function needs to do its job.

2. Lists: You're working with Python lists (recipe and ingredients). Lists are ordered collections of items. 
They are perfect for storing sequences of things, like ingredients in a recipe or items in an inventory.

3. Variables: You declare variables like correct (or match_count in your code) and missing to store information as the function runs. 
correct keeps track of how many ingredients match, and missing is a list that will hold the ingredients you couldn't find.

4. Iteration (for loop): The line for ingredient in recipe: is a for loop. This is how you go through each item in a list one by one. The loop will run once for every ingredient in the recipe list.

5. Membership Testing (in keyword): Inside the loop, if ingredient in ingredients: uses the in keyword. 
This is a very handy way to check if a specific item (ingredient) exists within another list (ingredients). It returns True if it's found, and False otherwise.

6. Conditional Logic (if/else): The if ingredient in ingredients: and else: structure is how you make decisions in code. 
If the ingredient is found in the ingredients list, the code inside the if block runs (correct += 1). If it's not found, the code inside the else block runs (missing.append(ingredient)).

7. List Appending: missing.append(ingredient) adds the current ingredient to the missing list. This happens when the ingredient from the recipe is not found in the ingredients list.

8. Arithmetic and Percentage Calculation: percentage = correct / len(recipe) * 100 calculates the percentage.

-len(recipe) gets the total number of items in the recipe list.
-correct / len(recipe) gives you the fraction of ingredients found (e.g., 3 out of 4 is 0.75).
-Multiplying by 100 converts that fraction into a percentage (e.g., 0.75 * 100 = 75.0).

9. Returning Multiple Values: return percentage, missing sends the final results back to wherever the function was called. 
In Python, you can simply separate values with a comma in the return statement, and they will be returned as a tuple (an ordered, immutable collection).

So, you've combined these concepts to iterate through the recipe, check which ingredients you have, count them, list the ones you don't, and calculate the required percentage!

"""