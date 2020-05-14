
animals_dict = {
    "rabbit": {
        "name": "rabbit",
        "name_ru": "Кролик",
        "food": 25,
        "damage": 0,
        "min_peaple": 3,
        "chance_damage": 3,
        "chance_find": 50,
    },
    "wild_boar": {
        "name": "wild_boar",
        "name_ru": "Дикий кабан",
        "food": 45,
        "damage": 20,
        "min_peaple": 5,
        "chance_damage": 15,
        "chance_find": 40,
    },
    "deer": {
        "name": "deer",
        "name_ru": "Олень",
        "food": 50,
        "damage": 15,
        "min_peaple": 7,
        "chance_damage": 10,
        "chance_find": 35,
    },
}

fish_dict = {
    "crabs": {
        "name": "crabs",
        "name_ru": "Краб",
        "food": 25,
        "damage": 3,
        "min_peaple": 1,
        "chance_damage": 0,
        "chance_find": 50,
    },
    "crucian": {
        "name": "crucian",
        "name_ru": "Карась",
        "food": 35,
        "damage": 3,
        "min_peaple": 2,
        "chance_damage": 0,
        "chance_find": 40,
    },
    "shark": {
        "name": "shark",
        "name_ru": "Акула",
        "food": 50,
        "damage": 30,
        "min_peaple": 5,
        "chance_damage": 20,
        "chance_find": 30,
    },
}


greens_dict = {
    "apple": {
        "name": "apple",
        "name_ru": "Яблоко",
        "food": 25,
        "damage": 5,
        "min_peaple": 2,
        "chance_damage": 0,
        "chance_find": 40,
    },
    "banana": {
        "name": "banana",
        "name_ru": "Банан",
        "food": 30,
        "damage": 5,
        "min_peaple": 2,
        "chance_damage": 0,
        "chance_find": 40,
    },
    "cereal": {
        "name": "cereal",
        "name_ru": "Зерно",
        "food": 35,
        "damage": 5,
        "min_peaple": 3,
        "chance_damage": 2,
        "chance_find": 40,
    },
}


# def gen_animal_list(n):
#     list_animal = []
#     for i in range(n):
#         animals_dict.update(fish_dict)
#         key = random.choice(list(animals_dict.keys()))
#         obj = animals_dict[key]
#         list_animal.append(type(key, (), obj))
#
#     return list_animal
#
#
# if __name__ == '__main__':
#     list_animal = gen_animal_list(5)
#
#     for i in list_animal:
#         print(i.name)
