from collections import Counter

# Load existing ingredients
with open("valid_ingredients.txt", "r", encoding="utf-8") as file:
    ingredients = [line.strip().lower() for line in file if line.strip()]

# Extract just the first word of each ingredient
base_ingredients = [line.split()[0] for line in ingredients]

# Optionally filter common ones only
counts = Counter(base_ingredients)
filtered = sorted(set([word for word, count in counts.items() if count >= 2 or len(word) > 3]))

# Save to new file
with open("simplified_valid_ingredients.txt", "w", encoding="utf-8") as file:
    for ingredient in filtered:
        file.write(f"{ingredient}\n")

print("Simplified ingredient list saved to simplified_valid_ingredients.txt")
