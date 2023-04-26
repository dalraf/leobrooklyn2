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
        self.map_shotting = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        self.map_attacking = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
        self.map = self.map_stopped
        self.walking = "walking"
        self.stopped = "stopped"
        self.shotting = 'shotting'
        self.attacking = 'attacking'
        self.status = self.stopped
        self.old_status = self.stopped
        self.freeze_map = False

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
    
    def walk_shotting(self):
        self.status = self.shotting

    def walk_attacking(self):
        self.status = self.attacking

    def walk_stopped(self):
        self.status = self.stopped

    def verify_freeze_map(self, active=False):
        if active:
            self.freeze_map = True
        if self.freeze_map:
            if (self.index_map // self.sprint) < (len(self.map) - 1):
                return False
            else:
                self.freeze_map = False
                return True
        else:
            return True

    def define_map(self):
        if self.verify_freeze_map():
            if self.status != self.old_status:
                self.index_map = 0
                self.old_status = self.status

            if self.status == self.stopped:
                self.map = self.map_stopped

            if self.status == self.walking:
                self.map = self.map_walking

            if self.status == self.shotting:
                self.map = self.map_shotting
                self.verify_freeze_map(active=True)

            if self.status == self.attacking:
                self.map = self.map_attacking
                self.verify_freeze_map(active=True)


    def draw(self):
        self.define_map()
        self.index_map = (self.index_map + 1) % (len(self.map) * self.sprint)
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
