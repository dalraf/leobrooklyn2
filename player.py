class Player:
    def __init__(self, pyxel, tile_map):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.tile_size = 48
        self.w = self.tile_size
        self.h = self.tile_size
        self.x = 0
        self.y = 0
        self.walk_fator = 10
        self.index_map = 0
        self.sprint = 3
        self.map_stopped = [(4, 2), (0, 3), (1, 3), (2, 3)]
        self.map_walking = [(3, 3), (4, 3), (0, 4), (1, 4)]
        self.map = self.map_stopped
        self.walking = 'walking'
        self.stopped = 'stopped'
        self.status = self.stopped

    def tile_coord(self, x, y):
        return x * self.tile_size, y * self.tile_size

    def flip_left(self):
        if self.w > 0:
            self.w *= -1

    def flip_right(self):
        if self.w < 0:
            self.w *= -1

    def walk_right(self):
        self.flip_right()
        self.x += self.walk_fator
        self.status = self.walking

    def walk_left(self):
        self.flip_left()
        self.x -= self.walk_fator
        self.status = self.walking

    def walk_up(self):
        self.y -= self.walk_fator
        self.status = self.walking

    def walk_down(self):
        self.y += self.walk_fator
        self.status = self.walking

    def walk_stopped(self):
        self.status = self.stopped

    def define_map(self):
        if self.status == self.stopped:
            self.map = self.map_stopped
        
        if self.status == self.walking:
            self.map = self.map_walking

    def draw(self):
        self.define_map()
        self.index_map = (self.index_map + 1) % (
            len(self.map) * self.sprint
        )
        self.tile_pos_x, self.tile_pos_y = self.tile_coord(
            *self.map[self.index_map // self.sprint]
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
