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
    return(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_qty_dict = {}
    for dish in dishes:
        dish1 = dish.strip() #переменная dish после strip()
        for dish_from_book in get_cook_book().items():
            dish2 = dish_from_book[0].strip() #переменная dish_from_book после strip()
            if dish1 == dish2:
                for ingredient in dish_from_book[1]:
                    ingredient_parameters_dict = {}
                    if ingredient['ingredient_name'] in ingredients_qty_dict:
                        ing_parameters = ingredients_qty_dict[ingredient['ingredient_name']]
                        qty = ing_parameters['quantity']
                        ingredient_parameters_dict['quantity'] = int(ingredient['quantity']) * person_count +qty
                    else:
                        ingredient_parameters_dict['quantity'] = int(ingredient['quantity']) * person_count
                    ingredient_parameters_dict['measure'] = ingredient['measure']
                    ingredients_qty_dict[ingredient['ingredient_name']] = ingredient_parameters_dict
    print(ingredients_qty_dict)




dishes = input("Введите названия блюд: ").split(sep=',')
person_count = int(input("Введите количество персон: "))
get_shop_list_by_dishes(dishes, person_count)
