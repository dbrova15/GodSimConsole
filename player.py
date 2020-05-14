

class Player:
    def __init__(self):
        # self.delta_animal_chance_find = 0.4
        # self.delta_fish_chance_find = 0.4
        # self.delta_green_chance_find = 0.4
        self.nature = None
        self.faith = 20

    def add_faith(self, n):
        self.faith += n
        if self.faith > 100:
            self.faith = 100
        elif self.faith < 0:
            self.faith = 0

    def add_nature(self, nature):

        self.nature = nature

    def check_faith(self, n):
        a = self.faith - n
        if a >= 0:
            return True
        else:
            return False

    def get_delta_animal(self, nature):
        res = nature.get_weather()
        k = res[1]['d_animal'] / 100
        # k = res[1]['d_animal'] * self.delta_animal_chance_find / 100

        # self.delta_animal_chance_find += self.delta_animal_chance_find * k
        # print(self.delta_animal_chance_find)
        # return self.delta_animal_chance_find
        return k

    def get_delta_fish(self, nature):
        res = nature.get_weather()
        k = res[1]['d_fish'] / 100
        # k = res[1]['d_fish'] * self.delta_fish_chance_find / 100

        # self.delta_fish_chance_find += self.delta_fish_chance_find * k
        # print(self.delta_fish_chance_find)
        # return self.delta_fish_chance_find
        return k

    def get_delta_green(self, nature):
        res = nature.get_weather()
        k = res[1]['d_green'] / 100
        # k = res[1]['d_green'] * self.delta_green_chance_find / 100

        # self.delta_green_chance_find += self.delta_green_chance_find * k
        # print(self.delta_green_chance_find)
        # return self.delta_green_chance_find
        return k


if __name__ == '__main__':
    player = Player()
    player.get_delta_animal()
