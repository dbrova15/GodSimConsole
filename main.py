# from animals import gen_animal_list
import random

from termcolor import colored

from house import House
from human import Human, specialization
from nature import Nature
from player import Player
from village import Village
from world import World

# todo расширить вывод информации о жителях
# todo добавить случайные события ( засуха, дождь, и тд)
# todo добавить бодель игрока с возможностью творить чудеса (дождь, стадо животных, и тд)


class Game:
    def __init__(self):
        self.menu = """
        Меню:
            1) Показать общую статистику о деревне
            2) Следующий день
            3) Изменить погоду
            4) Закончить игру
        """

        self.day = 1

        self.village = Village()
        self.player = Player()
        self.nature = Nature()
        self.world = World()
        self.world.add_nature(self.nature)
        self.world.add_player(self.player)
        self.village.add_player(self.player)

        for i in range(5):
            house = House()
            self.village.add_house(house)

        index = 1
        start_specialization = specialization
        list_spec = []
        for house in self.village.houses:
            for i in range(2):
                human = Human()
                spec = random.choice(start_specialization)
                list_spec.append(spec)
                if list_spec.count(spec) >= 4:
                    start_specialization.remove(spec)

                human.specialization = spec
                index += 1
                house.add_people(human)

        self.world.add_worker(self.village.get_people())

    def get_satiety_peaple(self):
        list_sat = []
        list_health = []
        list_name = []
        for hum in self.village.get_people():
            list_sat.append(hum.satiety)
            list_health.append(hum.health)
            list_name.append(hum.name)
        # print(list_sat)
        # print(list_health)
        # print(list_name)

    def check_new_peaple(self):
        part_food = self.village.get_surplus_food2()
        # print("part_food", part_food)
        if part_food >= 6:
            human = Human()
            self.village.add_human(human)
            faith = 10
            self.player.add_faith(faith)
            print(colored("Житель {} прибыл в деневню. Вера увеличилась на {}".format(human.name, faith), "cyan"))

    def print_stat(self):
        dict_stat = self.village.short_paeple_statistic()
        short_stat_text = """Среднее здоровье людей: {}\nСредняя сытость людей: {}\nСреднее счастье людей: {}\nКоличество больных людей: {}\nВера: {}\nКоличество охотников: {}\nКоличество рыбаков {} \nКоличество собирателей {}""".format(
            dict_stat['health_peaple'], dict_stat['satiety_peaple'],
            dict_stat['fun_peaple'], dict_stat['illnesses_peaple'], dict_stat['faith'],
            dict_stat['hunters'],
            dict_stat['fisherman'],
            dict_stat['collectors'],
        )
        print(short_stat_text)

    def run(self):
        while True:
            print("\nДень: {}".format(self.day))
            print(self.village.news())
            print("Погода сейчас: {}".format(self.nature.weather_now_ru))
            self.get_satiety_peaple()
            print("Вера: {}".format(self.player.faith))
            print(self.menu)
            r = input("Твоя команда?: ")
            if r == '1':
                self.print_stat()
                # while True:
                #     r_stat = input("1) Назад\nТвоя команда?: ")
                #     if r_stat == '1':
                #         break
            elif r == '2':
                self.check_new_peaple()
                self.world.add_worker(self.village.get_people())
                self.nature.next_day()
                food = self.world.next_day()
                self.village.food += food
                self.village.next_day()

                col_peaple = self.village.check_peaple()
                if col_peaple == 0:
                    print(colored("Все жители умерли. Конец игры!", "red"))
                    break

                self.day += 1
            elif r == '3':
                print(self.nature.get_weather_info())
                while True:
                    print("&!" * 10)
                    rate = input("На пунктов изменить погоду?\nОт -50 до 50. 1 пункт равен 3 манны.\nОтвет: ")
                    if -50 <= int(rate) <= 50:
                        self.nature.add_weather_rate(int(rate))
                        self.player.faith -= abs(int(rate) * 3)
                        print("Уровень веры: ", self.player.faith)
                        print(self.nature.get_weather_info())
                        break
            # elif r == '5':
            #     print(self.nature.get_weather_info())
            #     self.nature.add_weather_rate(random.randint(-10, -50))
            elif r == '4':
                break
            else:
                print(colored("Я не знаю такой команды", "red"))


if __name__ == '__main__':
    Game().run()
