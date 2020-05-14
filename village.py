import random

from termcolor import colored


class Village:
    def __init__(self):
        self.food = 120
        self.houses = []
        self.illnesses = []
        self.animals = []
        self.player = None

    def add_player(self, player):
        self.player = player

    def add_human(self, man):
        house = random.choice(self.houses)
        house.add_people(man)
        man.house = house

    def get_surplus_food(self):
        all_peaple = len(self.get_people())
        norma_food_day = 4 * all_peaple
        surplus_food = (self.food / 3 - norma_food_day) / all_peaple
        return surplus_food

    def get_surplus_food2(self):
        all_peaple = len(self.get_people())
        norma_food_day = 4 * all_peaple
        surplus_food = (self.food - norma_food_day * 3) / all_peaple
        return surplus_food

    def get_food_for_one(self):
        all_peaple = len(self.get_people())
        up_portion_food = 0
        norma_food_day = 4 * all_peaple

        portion_food = self.food / 3 / all_peaple
        if portion_food > 4:
            surplus_food = self.food - norma_food_day * 3
            up_portion_food = surplus_food / all_peaple

        portion_food += up_portion_food
        if portion_food < 1:
            portion_food = 1
        elif portion_food > 6:
            portion_food = 6
        return portion_food

    def add_house(self, house):
        self.houses.append(house)

    def add_illness(self, illness):
        self.illnesses.append(illness)

    def remove_illness(self, illness):
        self.illnesses.remove(illness)

    def get_people(self):
        list_peaple = []
        for i in self.houses:
            list_peaple.extend(i.people)
        return list_peaple

    def check_peaple(self):

        for h in self.houses:
            hum_list = h.people
            for hum in hum_list:
                if hum.health < 0:
                    faith = -20
                    h.remove_peaple(hum)
                    print(colored("Житель {} умер. Вера уменьшилась на {}".format(hum.name, faith), "red"))
                    self.player.add_faith(-20)

        return len(self.get_people())

    def separate_sex(self):
        women_list = []
        men_list = []

        for hum in self.get_people():
            if hum.man is True:
                men_list.append(hum)
            else:
                women_list.append(hum)

        return men_list, women_list

    def next_day(self):
        eaten_food = 0
        portion_food = self.get_food_for_one()
        if portion_food > 4:
            faith = round(portion_food * 0.5, 2)
            self.player.add_faith(faith)
            print("Люди живут в достатке. Вера увеличилась на {}".format(faith))
        elif portion_food < 3:
            faith = round(portion_food * -1, 2)
            self.player.add_faith(faith)
            print("Людям не хватает еды. Вера уменьшилась на {}".format(faith))
        else:
            faith = 2
            self.player.add_faith(faith)
            print("Людям хватает еды чтобы не умереть. Вера увеличилась на {}".format(faith))

        # print("portion_food", portion_food)
        for hum in self.get_people():
            hum.next_day()
            hum.eat(portion_food)
            eaten_food += portion_food
        # print("eaten_food", eaten_food)

        res_food = int(self.food - eaten_food)
        if res_food < 0:
            self.food = 0
        else:
            self.food = res_food

    def news(self):
        peaple = self.get_people()
        men_list, women_list = self.separate_sex()
        news = """Еда: {}, Людей: {}, Мужчин: {}, Женщин: {}""".format(self.food, len(peaple), len(men_list), len(women_list))
        return news

    def paeple_statistic(self):
        stat_peaple = {}
        for hum in self.get_people():
            stat_peaple[hum.name] = hum.house_statistic

        return stat_peaple

    def short_paeple_statistic(self):
        health_peaple_list = []
        satiety_peaple_list = []
        fun_peaple_list = []
        illnesses_peaple_list = []
        hanter_list = []
        fishermens_list = []
        collectors_list = []

        faith = 0
        for hum in self.get_people():
            health_peaple_list.append(hum.health)
            satiety_peaple_list.append(hum.satiety)
            fun_peaple_list.append(hum.fun)
            if len(hum.illnesses) > 0:
                illnesses_peaple_list.append(hum)
            faith += hum.faith
            if hum.specialization == "hunter":
                hanter_list.append(hum)
            elif hum.specialization == "fisherman":
                fishermens_list.append(hum)
            elif hum.specialization == "collector":
                collectors_list.append(hum)

        return {
            "health_peaple": sum(health_peaple_list) / len(health_peaple_list),
            "satiety_peaple": sum(satiety_peaple_list) / len(satiety_peaple_list),
            "fun_peaple": sum(fun_peaple_list) / len(fun_peaple_list),
            "illnesses_peaple": len(illnesses_peaple_list),
            "faith": faith,
            "hunters": len(hanter_list),
            "fisherman": len(fishermens_list),
            "collectors": len(collectors_list),
        }

    def houses_statistic(self):
        stat_houses = {}
        for h in self.houses:
            stat_houses[h.owner] = h.health

        return stat_houses