import datetime
from buiding import Building
from rock import Rock_Player, Rock_Enemy
from static_objects import Static_Object


class Objects:
    def __init__(
        self,
        pyxel,
        tile_map,
        game_witht,
        game_height,
    ):
        self.game_witdh = game_witht
        self.game_height = game_height
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.lista_objects = [
            Building(pyxel, tile_map, game_witht, game_height),
            Static_Object(pyxel, tile_map, game_witht, game_height),
        ]

    def add_rock_player(self, x, y, direction=1):
        self.lista_objects.append(Rock_Player(self.pyxel, self.tile_map, x, y, direction))

    
    def add_rock_enemy(self, x, y, direction=1):
        self.lista_objects.append(Rock_Enemy(self.pyxel, self.tile_map, x, y, direction))


    def update(self, player):
        for object in self.lista_objects:
            if object.killed:
                self.lista_objects.remove(object)
                del object
            else:
                object.update(player)

    def draw(self):
        for object in self.lista_objects:
            if not object.killed:
                object.draw()
