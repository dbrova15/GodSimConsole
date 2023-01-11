import random


delta_animal_chance_find = 0.3
delta_fish_chance_find = 0.3
delta_green_chance_find = 0.3

nature_dict = {
    "dry": {
        'd_animal': int(40 * delta_animal_chance_find),
        'd_fish': int(70 * delta_fish_chance_find),
        'd_green': int(40 * delta_green_chance_find),
        'ru': "засуха"
    },
    "sunshine": {
        'd_animal': int(70 * delta_animal_chance_find),
        'd_fish': int(100 * delta_fish_chance_find),
        'd_green': int(70 * delta_green_chance_find),
        'ru': 'солнечно'
    },
    "mid": {
        'd_animal': int(100 * delta_animal_chance_find),
        'd_fish': int(100 * delta_fish_chance_find),
        'd_green': int(100 * delta_fish_chance_find),
        'ru': 'умерено'
    },
    "rain": {
        'd_animal': int(70 * delta_animal_chance_find),
        'd_fish': int(120 * delta_fish_chance_find),
        'd_green': int(150 * delta_fish_chance_find),
        'ru': "дождь"
    },
    "storm": {
        'd_animal': int(50 * delta_animal_chance_find),
        'd_fish': int(90 * delta_fish_chance_find),
        'd_green': int(20 * delta_fish_chance_find),
        'ru': 'шторм'
    },
}


class Nature:
    def __init__(self):
        self.god_word = False
        self.weather_now = "mid"
        self.weather_now_ru = nature_dict[self.weather_now]['ru']
        self.weather_offset = 0
        self.weather_rate = 50
        self.weather_dict = {"dry": (0, 15),
                             "sunshine": (15, 35),
                             "mid": (35, 65),
                             "rain": (65, 85),
                             "storm": (85, 100)}

    def next_day(self):
        if self.god_word is False:
            self.change_weather_rate()
        self.god_word = False
        # print("next_day", self.weather_rate)

    def change_weather_rate(self):
        rate = self.weather_rate
        rate += random.randint(-50, 50)
        if rate < 0:
            rate = 0
        elif rate > 100:
            rate = 100
        self.weather_rate = rate

    def add_weather_rate(self, rate):
        self.god_word = True
        self.weather_rate += rate

    def get_weather_info(self):
        w = self.weather_now
        limits_tuple = list(self.weather_dict[w])
        nk = list(nature_dict.keys()).index(w)
        info_now = "Погода сейчас: {}, пунктов погоды сейчас {}, вероятность успеха охоты: {} %, вероятность успеха рыбалки: {} %, вероятность успеха собирательства: {} %".format(nature_dict[w]["ru"], self.weather_rate,
                                                                                                            nature_dict[w]['d_animal'],
                                                                                                            nature_dict[w]['d_fish'],
                                                                                                            nature_dict[w]['d_green'],
                                                                                                            )

        if nk == 0:
            info_minus = '--//--'
            point_plus = limits_tuple[1]
            name_weather = list(self.weather_dict.keys())[1]
            info_plus = "Следующий уровень: {}, пунктов погоды сейчас {}, вероятность успеха охоты: {} %, вероятность успеха рыбалки: {} %, вероятность успеха собирательства: {} %".format(nature_dict[name_weather]['ru'], point_plus,
                                                                                                            nature_dict[name_weather]['d_animal'],
                                                                                                            nature_dict[name_weather]['d_fish'],
                                                                                                            nature_dict[name_weather]['d_green'],
                                                                                                            )
        elif nk == 4:
            info_plus = "--//--"
            point_minus = limits_tuple[0]
            name_weather = list(self.weather_dict.keys())[3]
            info_minus = "Предыдущий уровень: {}, пунктов погоды сейчас {}, вероятность успеха охоты: {} %, вероятность успеха рыбалки: {} %, вероятность успеха собирательства: {} %".format(nature_dict[name_weather]['ru'], point_minus,
                                                                                                            nature_dict[name_weather]['d_animal'],
                                                                                                            nature_dict[name_weather]['d_fish'],
                                                                                                            nature_dict[name_weather]['d_green'],
                                                                                                            )
        else:
            point_minus = limits_tuple[0]
            point_plus = limits_tuple[1]
            name_weather_plus = list(self.weather_dict.keys())[nk + 1]
            name_weather_minus = list(self.weather_dict.keys())[nk - 1]
            info_minus = "Предыдущий уровень: {}, пунктов погоды сейчас {}, вероятность успеха погоды: {} %, вероятность успеха рыбалки: {} %, вероятность успеха собирательства: {} %".format(nature_dict[name_weather_minus]['ru'], point_minus,
                                                                                                            nature_dict[name_weather_minus]['d_animal'],
                                                                                                            nature_dict[name_weather_minus]['d_fish'],
                                                                                                            nature_dict[name_weather_minus]['d_green'],
                                                                                                            )
            info_plus = "Следующий уровень: {}, пунктов погоды сейчас {}, вероятность успеха погоды: {} %, вероятность успеха рыбалки: {} %, вероятность успеха собирательства: {} %".format(nature_dict[name_weather_plus]['ru'], point_plus,
                                                                                                            nature_dict[name_weather_plus]['d_animal'],
                                                                                                            nature_dict[name_weather_plus]['d_fish'],
                                                                                                            nature_dict[name_weather_plus]['d_green'])

        return "{}\n{}\n{}".format(info_minus, info_now, info_plus)

    def get_weather(self):
        for k in self.weather_dict.keys():
            if self.weather_dict[k][0] <= self.weather_rate <= self.weather_dict[k][1]:
                self.weather_now = k
                self.get_weather_info()
                return k, nature_dict[k]


if __name__ == '__main__':
    nature = Nature()
    res = nature.get_weather()
    print(res)
