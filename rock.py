import datetime
import random


class Rock:
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
        self.sprint = random.choice(range(3, 8))
        self.time_to_live = datetime.datetime.now()
        self.shoot_enemy = False
        self.shoot_player = False
        self.killed = False

    def tile_coord(self, x, y):
        return x * self.tile_size, y * self.tile_size

    def calculate_distance_damage(self, sprite):
        distance_x = (self.x + (self.w / 2)) - (sprite.x + (sprite.w * 0.5))
        distance_y = (self.y + (self.h / 2)) - (sprite.y + (sprite.h * 0.3))
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

