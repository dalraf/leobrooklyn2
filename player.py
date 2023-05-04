class Player:
    def __init__(self, pyxel, tile_map, game_witht, game_height, objects, camera):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.game_wight = game_witht
        self.game_height = game_height
        self.objects = objects
        self.camera =  camera
        self.camera_x = 0
        self.tile_size = 32
        self.w = self.tile_size
        self.h = self.tile_size
        self.x = 80
        self.y = game_height // 2
        self.walk_fator = 10
        self.index_map = 0
        self.sprint = 3
        self.explorer_map = [0, game_witht]
        self.top_walking = int(game_height * 0.5) 
        self.down_walking = (int(game_height * 0.96) - self.tile_size)
        self.left_walking = 0
        self.right_walking = game_witht
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
        self.life = 10
        self.killed = False

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
        if self.x + 80 >  self.camera_x + int(self.game_wight):
            self.camera_x += self.walk_fator
            self.camera(self.camera_x , 0)
        self.x += self.walk_fator
        self.status = self.walking
        if (self.x + self.tile_size) > self.explorer_map[1]:
            self.explorer_map[1] += self.walk_fator

    def walk_left(self):
        self.flip_left()
        if self.x - 80 <  self.camera_x:
            self.camera_x -= self.walk_fator
            self.camera(self.camera_x , 0)
        self.x -= self.walk_fator
        self.status = self.walking
        if self.x < self.explorer_map[0]:
            self.explorer_map[0] -= self.walk_fator

    def walk_up(self):
        if self.y >= self.top_walking:
            self.y -= self.walk_fator
            self.status = self.walking
        else:
            self.status = self.stopped


    def walk_down(self):
        if self.y <= self.down_walking:
            self.y += self.walk_fator
            self.status = self.walking
        else:
            self.status = self.stopped
    
    def walk_shotting(self):
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

    def verify_shotting(self):
        if self.map == self.map_shotting:
            if (self.index_map // self.sprint) == (len(self.map) - 1):
                if self.w > 0:
                        direction = 1
                if self.w < 0:
                    direction = -1

                if direction > 0:
                    x = self.x + 40
                if direction < 0:
                    x = self.x - 10
                y = self.y + 10
                self.objects.add_rock_player(x, y, direction)

    def update(self):
        self.define_map()
        self.index_map = (self.index_map + 1) % (len(self.map) * self.sprint)
        self.verify_shotting()
        self.tile_pos_x, self.tile_pos_y = self.tile_coord(
            *self.map[self.index_map // self.sprint]
        )
    
    def draw(self):
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
