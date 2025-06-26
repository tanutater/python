import pyinputplus as pyip

# Prices
bread_prices = {'wheat': 1.5, 'white': 1.0, 'sourdough': 1.8}
protein_prices = {'chicken': 2.5, 'turkey': 2.7, 'ham': 2.3, 'tofu': 2.0}
cheese_prices = {'cheddar': 1.0, 'swiss': 1.2, 'mozzarella': 1.1}
extras_prices = {'mayo': 0.2, 'mustard': 0.2, 'lettuce': 0.3, 'tomato': 0.3}

# Bread
prompt1 = "Bread type: wheat, white, or sourdough.\n"
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt=prompt1,numbered=True)
bread_cost = bread_prices[bread]

# Protein
prompt2 = "Protein type: chicken, turkey, ham, or tofu.\n"
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt=prompt2,numbered=True)
protein_cost = protein_prices[protein]

# Cheese (optional)
prompt3 = "Want cheese? (yes or no)\n"
cheese_cost = 0
cheese = None
if pyip.inputYesNo(prompt3) == 'yes':
    prompt4 = "Cheese type: cheddar, Swiss, or mozzarella\n"
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt=prompt4,numbered=True)
    cheese_cost = cheese_prices[cheese]

# Extra (optional)
prompt5 = "Want mayo, mustard, lettuce, or tomato? (yes or no)\n"
extra_cost = 0
extra = None
if pyip.inputYesNo(prompt5) == 'yes':
    prompt6 = "Choose one extra item:\n"
    extra = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], prompt=prompt6,numbered=True)
    extra_cost = extras_prices[extra]

# Quantity
quantity = pyip.inputInt("How many sandwiches would you like? (min 1):\n", min=1)

# Total calculation
single_sandwich_cost = bread_cost + protein_cost + cheese_cost + extra_cost
total_cost = quantity * single_sandwich_cost

# Output summary
print("\n--- Order Summary ---")
print(f"Bread: {bread} (${bread_cost:.2f})")
print(f"Protein: {protein} (${protein_cost:.2f})")
if cheese:
    print(f"Cheese: {cheese} (${cheese_cost:.2f})")
if extra:
    print(f"Extra: {extra} (${extra_cost:.2f})")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost:.2f}")
