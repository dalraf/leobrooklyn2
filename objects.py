import datetime

class Pedra():
    def __init__(self, pyxel, tile_map, x, y, direction):
        self.pyxel = pyxel
        self.map = (1,0)
        self.tile_map = tile_map
        self.tile_size = 8
        self.w = self.tile_size
        self.h = self.tile_size
        self.x = x
        self.y = y
        self.direction = direction
        self.sprint = 5

    def tile_coord(self, x, y):
        return x * self.tile_size, y * self.tile_size
    
    def draw(self):
        self.x += self.direction * self.sprint
        self.tile_pos_x, self.tile_pos_y = self.tile_coord(
            *self.map
        )
        self.pyxel.blt(
            self.x,
            self.y,
            self.tile_map,
            self.tile_pos_x,
            self.tile_pos_y,
            self.w,
            self.h,
        )


        

class Objects():
    def __init__(self, pyxel, tile_map):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.lista_objects = []
        self.time_armed = datetime.datetime.now()

    def add_pedra(self, x, y, direction=1):
        if (datetime.datetime.now() - self.time_armed).seconds >= 1:
            self.lista_objects.append(Pedra(self.pyxel, self.tile_map, x , y, direction))
            self.time_armed = datetime.datetime.now()

    def draw(self):
        for object in self.lista_objects:
            object.draw()
        