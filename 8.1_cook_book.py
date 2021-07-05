from pprint import pprint


def get_cook_book():
    cook_dict = {}
    with open("recipes.txt", "r", encoding="utf-8") as file:
        cook_book = {}

        for line in file:
            dish_name = line.strip()
            ing_qty = file.readline().strip()
            ing_qty = int(ing_qty)

            dish_ings = []
            for ing_details in range(ing_qty):
                ing_params ={}

                ing_details = file.readline().strip()
                data = ing_details.split(sep='|')
                ing_params['ingredient_name'] = data[0]
                ing_params['quantity'] = data[1]
                ing_params['measure'] = data[2]
                dish_ings.append(ing_params)
            cook_book[dish_name] = dish_ings
            file.readline()
        print("cook_book = ", cook_book)
get_cook_book()
