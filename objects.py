import datetime


class Pedra:
    def __init__(self, pyxel, tile_map, x, y, direction):
        self.pyxel = pyxel
        self.map = (1, 0)
        self.tile_map = tile_map
        self.tile_size = 8
        self.w = self.tile_size
        self.h = self.tile_size
        self.x = x
        self.y = y
        self.direction = direction
        self.sprint = 5
        self.time_to_live = datetime.datetime.now()

    def tile_coord(self, x, y):
        return x * self.tile_size, y * self.tile_size

    def draw(self, game_witht, game_height, player):
        if (datetime.datetime.now() - self.time_to_live).seconds <= 3:
            self.x += self.direction * self.sprint
            self.x -= player.paralaxe
            self.tile_pos_x, self.tile_pos_y = self.tile_coord(*self.map)
            self.pyxel.blt(
                self.x,
                self.y,
                self.tile_map,
                self.tile_pos_x,
                self.tile_pos_y,
                self.w,
                self.h,
            )
        else:
            pass


class Building_1:
    def __init__(self, pyxel, tile_map, x, y):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.x = x
        self.y = y
        self.tile_pos_x = 0
        self.tile_pos_y = 8
        self.w = 58
        self.h = 64

    def draw(self, game_witht, game_height, player):
        self.x -= player.paralaxe
        self.pyxel.blt(
            self.x,
            self.y,
            self.tile_map,
            self.tile_pos_x,
            self.tile_pos_y,
            self.w,
            self.h,
            0
        )


class Objects:
    def __init__(self, pyxel, tile_map):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.lista_objects = []
        self.time_armed = datetime.datetime.now()

    def add_pedra(self, x, y, direction=1):
        if (datetime.datetime.now() - self.time_armed).seconds >= 1:
            self.lista_objects.append(Pedra(self.pyxel, self.tile_map, x, y, direction))
            self.time_armed = datetime.datetime.now()

    def verify_build_create_chance(self):
        lista_building = [j for j in self.lista_objects if isinstance(j, Building_1)]
        if len(lista_building) > 0:
            return False
        else:
            return True

    def verifiy_build_coord(self):
        x = 0
        y = self.player.top_walking - 64 + self.player.tile_size
        return x, y

    def create_building(self):
        if self.verify_build_create_chance():
            self.lista_objects.append(
                Building_1(self.pyxel, self.tile_map, *self.verifiy_build_coord())
            )

    def draw(self, game_witht, game_height, player):
        self.player = player
        self.create_building()
        self.player = player
        for object in self.lista_objects:
            object.draw(game_witht, game_height, player)
