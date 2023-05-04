import datetime
import random


class Rock_Player:
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
        self.sprint = random.choice(range(8, 15))
        self.time_to_live = datetime.datetime.now()
        self.killed = False

    def tile_coord(self, x, y):
        return x * self.tile_size, y * self.tile_size

    def calculate_distance_damage(self, sprite):
        med_x1 = (self.x + self.w) / 2
        med_y1 = (self.y + self.h) / 2
        med_x2 = (sprite.x + sprite.w) / 2
        med_y2 = (sprite.y + sprite.h) / 2
        distance_x = med_x1 - med_x2
        distance_y = med_y1 - med_y2
        mod = self.pyxel.sqrt(distance_x**2 + distance_y**2)
        return mod
    
    def update(self, player):
        if (datetime.datetime.now() - self.time_to_live).seconds <= 1:
            self.x += self.direction * self.sprint
            self.tile_pos_x, self.tile_pos_y = self.tile_coord(*self.map)
        else:
            self.killed = True

    def draw(self):
            if not self.killed:
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

class Rock_Enemy(Rock_Player):
    def __init__(self, pyxel, tile_map, x, y, direction):
        super().__init__(pyxel, tile_map, x, y, direction)
