shopping_dict = {"piekarnia":["chleb", "bułki", "pączek"], "warzywniak":["machew", "seler", "rukola"]}

number_of_products = 0
for key in shopping_dict:
    print(f"Ide do {str(key).capitalize()} i kupuje: {list(map(str.capitalize, shopping_dict[key]))}")
    number_of_products = number_of_products + len(shopping_dict[key])

print(f"W sumie kupuję {number_of_products} produktów.")
