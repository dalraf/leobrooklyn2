class Player:
    def __init__(self, pyxel, tile_map, game_witht, game_height, objects):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.objects = objects
        self.tile_size = 32
        self.w = self.tile_size
        self.h = self.tile_size
        self.x = 0
        self.y = game_height // 2
        self.walk_fator = 10
        self.index_map = 0
        self.sprint = 3
        self.paralaxe = 0
        self.top_walking = game_height // 3
        self.down_walking = (int(game_height * 0.90) - self.tile_size)
        self.left_walking = 0
        self.right_walking = game_witht - self.tile_size
        self.map_stopped = [(3, 5), (4, 5), (5, 5), (6, 5)]
        self.map_walking = [(7, 5), (0, 6), (1, 6), (2, 6)]
        self.map_shotting = [(5, 3), (6, 3), (7, 3), (0, 4), (1, 4)]
        self.map_attacking = [(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)]
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
        if self.x < self.right_walking:
            self.flip_right()
            self.x += self.walk_fator
            self.status = self.walking
            self.paralaxe = 0
        else:
            self.status = self.walking
            self.paralaxe = self.walk_fator

    def walk_left(self):
        if self.x > self.left_walking:
            self.flip_left()
            self.x -= self.walk_fator
            self.status = self.walking
            self.paralaxe = 0
        else:
            self.status = self.walking
            self.paralaxe = -self.walk_fator

    def walk_up(self):
        if self.y >= self.top_walking:
            self.y -= self.walk_fator
            self.status = self.walking
            self.paralaxe = 0
        else:
            self.status = self.stopped


    def walk_down(self):
        if self.y <= self.down_walking:
            self.y += self.walk_fator
            self.status = self.walking
            self.paralaxe = 0
        else:
            self.status = self.stopped
    
    def walk_shotting(self):
        if self.w > 0:
            direction = 1
        if self.w < 0:
            direction = -1

        if direction > 0:
            x = self.x + 40
        if direction < 0:
            x = self.x - 10
        
        y = self.y + 10

        self.objects.add_pedra(x, y, direction)
        self.status = self.shotting


    def walk_attacking(self):
        self.status = self.attacking

    def walk_stopped(self):
        self.status = self.stopped
        self.paralaxe = 0

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
            0
        )
