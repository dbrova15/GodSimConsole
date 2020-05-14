import random

from termcolor import colored


class House:
    def __init__(self):
        self.health = 100
        self.max_people = 3
        self.owner = None
        self.people = []

    def add_people(self, human):
        if len(self.people) == 0:
            self.owner = human
        elif len(self.people) >= self.max_people:
            print(colored("Максимальное количество жителей", "red"))
        self.people.append(human)

    def remove_peaple(self, human):
        self.people.remove(human)

        if human == self.owner and len(self.people) != 0:
            self.owner = random.choice(self.people)
        elif len(self.people) == 0:
            self.owner = None

    def get_info(self):
        men = []
        women = []
        for i in self.people:
            if i.fem == True:
                women.append(i)
            else:
                men.append(i)
        info = "Жителей: {}, Мужчин: {}, Женщин: {}".format(len(self.people), len(men), len(women))
        return info

    def house_statistic(self):
        stat_dict = {"owner": self.owner,
                     "health_house": self.health}

        return stat_dict