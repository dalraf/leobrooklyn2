import random


class Street_List:
    def __init__(self, pyxel, player, x_init):
        self.pyxel = pyxel
        self.player = player
        self.x_init = x_init
        self.w = 20
        self.h = 3
        self.tile_pos_x = 0
        self.tile_pos_y = 8
        self.calculate_x_y()

    def calculate_x_y(self):
        self.y = self.player.top_walking + int(self.player.top_walking * 0.55)
        if self.x_init < 0:
            self.x = self.x_init - self.w - 10

        if self.x_init > 0:
            self.x = self.x_init + 10

        if self.x_init == 0:
            self.x = 0
        

    def update(self):
        pass

    def draw(self):
        self.pyxel.rect(
            self.x,
            self.y,
            self.w,
            self.h,
            self.pyxel.COLOR_WHITE,
        )

class Static_Object:
    def __init__(self, pyxel, tile_map, game_witht, game_height):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.game_witht = game_witht
        self.game_height = game_height
        self.lista_Static_Object_left = []
        self.lista_Static_Object_right = []
        self.Static_Object_options = [Street_List,]
        self.killed = False

    def get_sum_size_Static_Object(self, lista):
        sum_Static_Object = sum([i.w + 20 for i in lista])
        if sum_Static_Object == None:
            sum_Static_Object = 0
        return sum_Static_Object

    def get_sum_size_Static_Object_left(self):
        return -1 * self.get_sum_size_Static_Object(self.lista_Static_Object_left) - 1

    def get_sum_size_Static_Object_right(self):
        return self.get_sum_size_Static_Object(self.lista_Static_Object_right)

    def update(self, player):
        self.explorer_map = player.explorer_map
        map_size_left = self.explorer_map[0] - 300
        map_size_right = self.explorer_map[1] + 300

        while map_size_right >= self.get_sum_size_Static_Object_right():
            Build_class = Street_List
            Static_Object_add = Build_class(
                self.pyxel, player, self.get_sum_size_Static_Object_right()
            )
            self.lista_Static_Object_right.append(Static_Object_add)

        while map_size_left <= self.get_sum_size_Static_Object_left():
            Build_class = Street_List
            Static_Object_add = Build_class(
                self.pyxel, player, self.get_sum_size_Static_Object_left()
            )
            self.lista_Static_Object_left.append(Static_Object_add)

        for object in self.lista_Static_Object_left:
            object.update()

        for object in self.lista_Static_Object_right:
            object.update()

    def draw(self):
        for object in self.lista_Static_Object_left:
            object.draw()

        for object in self.lista_Static_Object_right:
            object.draw()
