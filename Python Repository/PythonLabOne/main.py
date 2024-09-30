# Variable assignments
# Run this cell without changes
main = "rice"
protein = "salmon"
oz_of_protein = 4.5
number_of_sides = 3
side1 = 'seaweed'
side2 = 'onigiri'
side3 = 'turnip pickle'
great_bento = True

# Changing the protein
protein = "chicken"

# Changing the amount of protein to 3.5 oz
oz_of_protein = 3.5

# Update side order
side1, side2, side3 = "carrots", "kimchi", "mushrooms"

# Confirming changes of side orders
print("Updated sides:", side1, side2, side3)

# Check types of variables
print("Type of side1:", type(side1))
print("Type of oz_of_protein:", type(oz_of_protein))
print("Type of great_bento:", type(great_bento))

# If Else
if main == 'rice' and oz_of_protein > 2.5:
    great_bento = False
    print("No carbs, please, and too much protein!")
else:
    great_bento = True
    print("This bento box is great!")

# List operations
bento_ingredients = [main, protein, side1, side2, side3, "wasabi"]
print("Initial ingredients:", bento_ingredients)

# Accessing by index
print("Main ingredient:", bento_ingredients[0])

# Slicing the list
print("Sides in the bento:", bento_ingredients[2:5])

# Add an item and remove an item
bento_ingredients.append("ginger")
print("Added ginger:", bento_ingredients)
bento_ingredients.pop()  # Removes the last item
print("Removed last item:", bento_ingredients)

# Use join
print("I'd like my bento box to contain:", ", ".join(bento_ingredients[:-1]) + ", and " + bento_ingredients[-1])

# Using dictionaries
bento_dict = {
    "main": main,
    "protein": protein,
    "sides": bento_ingredients[2:5],
    "extra": bento_ingredients[5]
}

# Checking dictionary
print("Bento dictionary:", bento_dict)

# Accessing elements
print("Protein in the bento box:", bento_dict['protein'])

# Loop through dictionary and print each main
for key, value in bento_dict.items():
    if key == 'main':
        print(f"The main ingredient is {value}.")

print("Lists and loops could automate processing of repeated data entries such as customer orders in a restaurant.")
