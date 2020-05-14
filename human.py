import random

specialization = ["hunter", "fisherman", "collector"]


class Illness:
    def __init__(self):
        self.damage = 5  # повреждения
        self.time = 50  # тайминг повреждения
        self.symptoms = {}


class Human:
    def __init__(self, name=''):
        self.name = name
        self.ege = random.randint(15, 20)
        self.health = 80  # здоровье
        self.fun = 80  # развлечения
        self.satiety = 80  # сытость
        self.damage = 20  # урон
        self.man = random.choice([True, False])
        self.relations = {}  # отношения
        self.child = []  # дети
        self.illnesses = []  # болезни
        self.specialization = random.choice(specialization)  # работа
        self.action = None  # действия
        self.house = None
        self.faith = 10

        if len(self.name) < 2:
            self.set_random_name()

    def set_random_name(self):
        gender = self.man
        if gender:
            with open('name_man_ru.txt', 'r', encoding="utf-8") as f:
                name = random.choice(f.read().split("\n"))
        else:
            with open('name_woman_ru.txt', 'r', encoding="utf-8") as f:
                name = random.choice(f.read().split("\n"))
        # self.name = translit(name, 'ru')
        self.name = name
        # self.name = transliterate(name.strip())

    def set_specialization(self):
        if self.man is True:
            pass
        else:
            pass

    def statistic(self):
        if self.man is True:
            sex = "man"
        else:
            sex = 'woman'

        stat_dict = {
            "name": self.name,
            "man": self.man,
            "ege": self.ege,
            "health": self.health,
            "fun": self.fun,
            "satiety": self.satiety,
            "relations": self.relations,
            "child": self.child,
            "illnesses": self.illnesses,
            "specialization": self.specialization,
            "action": self.action
        }
        return stat_dict

    def add_contact(self, contact):
        self.relations[contact] = 0

    def add_health(self, hit):
        self.health += hit
        if self.health > 100:
            self.health = 100

    def add_satiety(self, sat):
        self.satiety += int(sat)
        if self.satiety > 100:
            self.satiety = 100
        elif self.satiety < 0:
            self.satiety = 0

    def next_day(self):
        self.add_satiety(-20)
        self.change_action()
        self.check_illness()

    def eat(self, food):
        set = food * 5

        if self.health < 30:
            self.add_health(food)

        self.add_satiety(set)

        if self.satiety > 95:
            self.add_health(10)
        elif self.satiety > 85:
            self.add_health(7)
        elif self.satiety > 70:
            self.add_health(5)
        elif self.satiety < 70:
            self.add_health(-5)
        elif self.satiety < 60:
            self.add_health(-10)
        elif self.satiety < 45:
            self.add_health(-20)
        elif self.satiety < 10:
            self.add_health(-30)

    def check_illness(self):
        pass

    def add_illness(self, illness):
        self.illnesses.append(illness)

    def remove_illness(self, illness):
        self.illnesses.pop(illness)

    def run_action(self):
        pass

    def change_action(self):

        if self.health < 40:
            self.action = "health"
        elif self.satiety < 50:
            self.action = "food"
        elif self.fun < 60:
            self.action = "fun"
        else:
            self.action = "work"


if __name__ == '__main__':
    human = Human()
