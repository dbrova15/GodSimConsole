import random

from termcolor import colored
from animals import animals_dict, fish_dict, greens_dict
from player import Player

# player = Player()


class World:
    def __init__(self):
        self.list_animals = []
        self.list_fishes = []
        self.list_greens = []

        self.hunters_list = []
        self.fisherman_list = []
        self.collectors_list = []

        # self.d_animal = 100
        # self.d_fish = 100
        # self.d_green = 100

        self.chance_damage = 5
        self.player = None
        self.nature = None
        self.faith_lost_prod = -3
        self.faith_empty = -5
        self.faith_delta_damage = -0.1

    def add_nature(self, nature):
        self.nature = nature

    def add_player(self, player):
        self.player = player

    def day_action(self):
        action_dict = {
            "hunting": self.hunting(),
            "fishing": self.fishing(),
            "gathering": self.gathering(),
        }
        return action_dict

    def hunting(self):
        damage_hunters = 0
        for h in self.hunters_list:
            damage_hunters += h.damage

        animal = self.get_animal()
        return self.food_action(damage_hunters, animal, self.hunters_list)

    def fishing(self):
        damage_fishermen = 0
        for h in self.fisherman_list:
            damage_fishermen += h.damage
        fish = self.get_fish()
        return self.food_action(damage_fishermen, fish, self.fisherman_list)

    def gathering(self):
        damage_collectors = 0
        for h in self.collectors_list:
            damage_collectors += h.damage
        green = self.get_green()
        return self.food_action(damage_collectors, green, self.fisherman_list)

    def food_action(self, damage_humans, obj, humans_list):

        action_dict = {}
        n = random.randint(1, 100)

        if n < obj.chance_find:
            self.chance_damage += obj.chance_damage
            if damage_humans > obj.damage:
                action_dict["obj"] = obj
                action_dict["food"] = obj.food
            else:
                action_dict["obj"] = obj
                action_dict["food"] = 0
        else:
            action_dict["obj"] = None

        if len(humans_list) != 0:
            random_human = random.choice(humans_list)
            damage = self.chance_damage_culc(self.chance_damage, random_human, obj)
        else:
            random_human = None
            damage = None

        action_dict['human'] = random_human
        action_dict['damage'] = damage
        return action_dict

    def chance_damage_culc(self, chance, human, obj):
        n = random.randint(1, 100)
        if chance < n:
            human.health -= obj.damage
            return obj.damage
        return 0

    def add_worker(self, peaple_list):
        self.hunters_list = []
        self.fisherman_list = []
        self.collectors_list = []

        for hum in peaple_list:
            if hum.specialization == "hunter":
                self.add_hanters(hum)
            elif hum.specialization == "fisherman":
                self.add_fishers(hum)
            elif hum.specialization == "collector":
                self.add_collectors(hum)
            else:
                pass

    def add_hanters(self, hunter):
        self.hunters_list.append(hunter)

    def add_fishers(self, fisherman):
        self.fisherman_list.append(fisherman)

    def add_collectors(self, collector):
        self.collectors_list.append(collector)

    def add_animals(self, animal):
        self.list_animals.append(animal)

    def add_fishes(self, fish):
        self.list_fishes.append(fish)

    def add_greens(self, green):
        self.list_greens.append(green)

    def get_animal(self):
        return random.choice(self.list_animals)

    def get_fish(self):
        return random.choice(self.list_fishes)

    def get_green(self):
        return random.choice(self.list_greens)

    def remove_animals(self, animal):
        self.list_animals.remove(animal)

    def remove_fishes(self, fish):
        self.list_fishes.remove(fish)

    def remove_greens(self, green):
        self.list_greens.remove(green)

    def gen_list_animals(self, n):
        delta_animal_chance_find = self.player.get_delta_animal(self.nature)
        for i in range(n):
            key = random.choice(list(animals_dict.keys()))
            obj = animals_dict[key]

            obj["chance_find"] = self.check_chance(obj, len(self.list_animals), delta_animal_chance_find)
            self.add_animals(type(key, (), obj))

    def gen_list_fishes(self, n):
        delta_fish_chance_find = self.player.get_delta_fish(self.nature)
        for i in range(n):
            key = random.choice(list(fish_dict.keys()))
            obj = fish_dict[key]
            obj["chance_find"] = self.check_chance(obj, len(self.list_fishes), delta_fish_chance_find)
            self.add_fishes(type(key, (), obj))

    def gen_list_greens(self, n):
        delta_green_chance_find = self.player.get_delta_green(self.nature)
        for i in range(n):
            key = random.choice(list(greens_dict.keys()))
            obj = greens_dict[key]
            obj["chance_find"] = self.check_chance(obj, len(self.list_greens), delta_green_chance_find)
            self.add_greens(type(key, (), obj))

    def check_chance(self, obj, count_humans, delta_chance):
        obj["chance_find"] += obj["chance_find"] * delta_chance
        if count_humans < obj['min_peaple']:
            obj["chance_find"] = obj["chance_find"] / 2
        return obj["chance_find"]

    def check_dead_human(self, hum):
        if hum.health <= 0:
            house = hum.house
            house.remove_peaple(hum)
            return True
        return False

    def result_day_action(self):
        res = self.day_action()
        # print(res)
        animal_food = fish_food = green_food = 0
        hunting = res['hunting']
        fishing = res['fishing']
        gathering = res['gathering']

        # print("hunters_list", len(self.hunters_list))
        # print("fisherman_list", len(self.fisherman_list))
        # print("collectors_list", len(self.collectors_list))

        print("&=" * 10)
        if hunting['human'] is not None:
            hunter_name = hunting['human'].name
            hunter_damage = hunting['damage']
            text_hunt_damage = ""
            if hunter_damage > 0:
                faith = round(hunter_damage * self.faith_delta_damage, 2)
                text_hunt_damage = colored("Охотник {} получил повреждения {}. Вера уменьшилась на {}".format(hunter_name, hunter_damage, faith),
                                           "yellow")
                self.player.add_faith(faith)

            if hunting['obj'] is not None:
                animal_name = hunting['obj'].name_ru
                animal_food = hunting['food']

                if animal_food != 0:
                    faith = round(animal_food * .3, 2)
                    text_res_hunt = colored(
                        "Охотники поймали {}. Получено {} едениц еды. Вера увеличилась на {}".format(animal_name, animal_food, faith), "cyan")
                else:
                    faith = self.faith_lost_prod
                    text_res_hunt = colored("Охотники наткнулись на {}, но упустили добычу. Вера уменьшилась на {}".format(animal_name, faith), "red")
            else:
                faith = self.faith_empty
                text_res_hunt = colored("Охота была не удачна. Вера уменьшилась на {}".format(faith), "red")
            print(text_res_hunt + " " + text_hunt_damage)
            self.player.add_faith(faith)
            if self.check_dead_human(hunting['human']):
                print(colored("Охотник {} погиб от полученых ран.".format(hunter_name), "red"))
        else:
            print("Нет охотников")

        if fishing['human'] is not None:
            fisherman_name = fishing['human'].name
            fisherman_damage = fishing['damage']
            text_fisher_damage = ""
            if fisherman_damage > 0:
                faith = round(fisherman_damage * self.faith_delta_damage, 2)
                text_fisher_damage = colored("Рыбак {} получил повреждения {}. Вера уменьшилась на {}".format(fisherman_name, fisherman_damage, faith),
                                             "yellow")
                self.player.add_faith(faith)

            if fishing['obj'] is not None:
                fish_name = fishing['obj'].name_ru
                fish_food = fishing['food']

                if fish_food != 0:
                    faith = round(fish_food * .3, 2)
                    text_res_fish = colored("Рыбаки поймали {}. Получено {} едениц еды. Вера увеличилась на {}".format(fish_name, fish_food, faith),
                                            "cyan")
                else:
                    faith = self.faith_lost_prod
                    text_res_fish = colored("Рыбаки наткнулись на {}, но упустили добычу. Вера уменьшилась на {}".format(fish_name, faith), "red")

            else:
                faith = self.faith_empty
                text_res_fish = colored("Рыбалка была не удачна. Вера уменьшилась на {}".format(faith), "red")
            print(text_res_fish + " " + text_fisher_damage)
            self.player.add_faith(faith)
            if self.check_dead_human(fishing['human']):
                print(colored("Рыбак {} погиб от полученых ран.".format(fisherman_name), "red"))
        else:
            print("Нет рыбаков")

        if gathering['human'] is not None:

            collector_name = gathering['human'].name
            collector_damage = gathering['damage']
            text_collect_damage = ""
            if collector_damage > 0:
                faith = round(collector_damage * self.faith_delta_damage, 2)
                text_collect_damage = colored(
                    "Собиратель {} получил повреждения {}. Вера уменьшилась на {}".format(collector_name, collector_damage, faith), "yellow")
                self.player.add_faith(faith)

            if gathering['obj'] is not None:
                green_name = gathering['obj'].name_ru
                green_food = gathering['food']

                if green_food != 0:
                    faith = round(green_food * .3, 2)
                    text_res_green = colored(
                        "Собиратели нашли {}. Получено {} едениц еды. Вера увеличилась на {}".format(green_name, green_food,faith), "cyan")

                else:
                    faith = self.faith_lost_prod
                    text_res_green = colored("Собиратели наткнулись на {}, но упустили добычу. Вера уменьшилась на {}".format(green_name, faith),
                                             "red")

            else:
                faith = self.faith_empty
                text_res_green = colored("Собиратели вернулись ни с чем. Вера уменьшилась на {}".format(faith), "red")

            print(text_res_green + " " + text_collect_damage)
            self.player.add_faith(faith)
            if self.check_dead_human(gathering['human']):
                print(colored("Собиратель {} погиб от полученых ран.".format(collector_name)), "red")
        else:
            print("Нет собирателей")

        food = animal_food + fish_food + green_food
        print("Собрано еды за день {}".format(food))
        return food

    def next_day(self):
        self.gen_list_animals(random.randint(1, 3))
        self.gen_list_fishes(random.randint(1, 3))
        self.gen_list_greens(random.randint(1, 3))

        food = self.result_day_action()
        #
        # self.player.add_faith(round(food * .3, 2))

        return food


if __name__ == '__main__':
    World()
