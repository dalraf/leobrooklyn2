import random

class Buildind_1:
    def __init__(self, pyxel, tile_map, player, x_init):
        self.pyxel = pyxel
        self.player = player
        self.tile_map = tile_map
        self.w = 115
        self.h = 128
        self.x = x_init
        self.y = self.player.top_walking - self.h + self.player.tile_size - 10
        self.tile_pos_x = 0
        self.tile_pos_y = 8

    def update(self, player):
        self.x -= player.paralaxe

    def draw(self):
        self.pyxel.blt(
            self.x,
            self.y,
            self.tile_map,
            self.tile_pos_x,
            self.tile_pos_y,
            self.w,
            self.h,
            0,
        )

class Building_2(Buildind_1):
    def __init__(self, pyxel, tile_map, player, x_init):
        super().__init__(pyxel, tile_map, player, x_init)
        self.tile_pos_x = 116
        self.tile_pos_y = 8
        self.w = 91
        self.h = 128

class Building_3(Buildind_1):
    def __init__(self, pyxel, tile_map, player, x_init):
        super().__init__(pyxel, tile_map, player, x_init)
        self.tile_pos_x = 209
        self.tile_pos_y = 6
        self.w = 38
        self.h = 128

class Building_4(Buildind_1):
    def __init__(self, pyxel, tile_map, player, x_init):
        super().__init__(pyxel, tile_map, player, x_init)
        self.tile_pos_x = 208
        self.tile_pos_y = 8
        self.w = 40
        self.h = 126

class Building_5(Buildind_1):
    def __init__(self, pyxel, tile_map, player, x_init):
        super().__init__(pyxel, tile_map, player, x_init)
        self.tile_pos_x = 197
        self.tile_pos_y = 8
        self.w = 52
        self.h = 64


class Building:
    def __init__(self, pyxel, tile_map, game_witht, game_height):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.game_witht = game_witht
        self.game_height = game_height
        self.lista_building_left = []
        self.lista_building_right = []
        self.building_options = [Buildind_1, Building_2, Building_3]

    def get_sum_size_building(self, lista):
        sum_building = sum([i.w + 10 for i in lista])
        if sum_building == None:
            sum_building = 0
        return sum_building

    def get_sum_size_building_left(self):
        return -1 * self.get_sum_size_building(self.lista_building_left)

    def get_sum_size_building_right(self):
        return self.get_sum_size_building(self.lista_building_right)

    def update(self, player):
        self.explorer_map = player.explorer_map
        map_size_left = self.explorer_map[0] - 300
        map_size_right = self.explorer_map[1] + 300
        while map_size_left < self.get_sum_size_building_left():
            Build_class = random.choice(self.building_options)
            building_add = Build_class(
                self.pyxel, self.tile_map, player, self.get_sum_size_building_left()
            )
            self.lista_building_left.append(building_add)
        while map_size_right > self.get_sum_size_building_right():
            Build_class = random.choice(self.building_options)
            building_add = Build_class(
                self.pyxel, self.tile_map, player, self.get_sum_size_building_right()
            )
            self.lista_building_right.append(building_add)

        for object in self.lista_building_left:
            object.update(player)

        for object in self.lista_building_right:
            object.update(player)

    def draw(self):
        for object in self.lista_building_left:
            object.draw()

        for object in self.lista_building_right:
            object.draw()
