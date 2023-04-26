class Player:
    def __init__(self, pyxel, tile_map):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.w = 64
        self.h = 64
        self.x = 0
        self.y = 0
        self.walk_fator = 10
        self.map_stopped = [(1, 3), (2, 3), (3, 3), (4, 3)]
        self.index_map = 0
        self.sprint = 2

    def tile_coord(self, x, y):
        return x * 64, y * 64

    def flip_left(self):
        if self.w > 0:
            self.w *= -1

    def flip_right(self):
        if self.w < 0:
            self.w *= -1

    def walk_right(self):
        self.flip_right()
        self.x += self.walk_fator

    def walk_left(self):
        self.flip_left()
        self.x -= self.walk_fator

    def walk_up(self):
        self.y -= self.walk_fator

    def walk_down(self):
        self.y += self.walk_fator

    def draw(self):
        self.index_map = (self.index_map + 1) % (len(self.map_stopped) * self.sprint)
        self.tile_pos_x, self.tile_pos_y = self.tile_coord(
            *self.map_stopped[int(self.index_map / self.sprint)]
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
