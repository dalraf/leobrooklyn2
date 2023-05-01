import datetime
from buiding import Building
from rock import Rock

class Objects:
    def __init__(self, pyxel, tile_map, game_witht, game_height,):
        self.game_witdh = game_witht
        self.game_height = game_height
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.building = Building(pyxel, tile_map, game_witht, game_height)
        self.lista_objects = [Building(pyxel, tile_map, game_witht, game_height),]
        self.time_armed = datetime.datetime.now()

    def add_rock(self, x, y, direction=1):
        if (datetime.datetime.now() - self.time_armed).seconds >= 1:
            self.lista_objects.append(Rock(self.pyxel, self.tile_map, x, y, direction))
            self.time_armed = datetime.datetime.now()


    def update(self, player):
        for object in self.lista_objects:
            if object.killed:
                del object
            else:
                object.update(player)

    def draw(self):
        for object in self.lista_objects:
            object.draw()
