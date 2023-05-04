import random


class Enemy_1:
    def __init__(self, pyxel, tile_map, game_witht, game_height, objects, player):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.game_wight = game_witht
        self.game_height = game_height
        self.objects = objects
        self.player = player
        self.tile_size = 32
        self.w = self.tile_size
        self.h = self.tile_size
        self.x = self.player.camera_x + self.game_wight
        self.y = game_height // 2
        self.walk_fator = 10
        self.index_map = 0
        self.sprint = 3
        self.explorer_map = [0, game_witht]
        self.top_walking = int(game_height * 0.5)
        self.down_walking = int(game_height * 0.96) - self.tile_size
        self.left_walking = 0
        self.right_walking = game_witht
        self.map_stopped = [(3, 5), (4, 5), (5, 5), (6, 5)]
        self.map_walking = [(7, 5), (0, 6), (1, 6), (2, 6)]
        self.map_shotting = [(5, 3), (6, 3), (7, 3), (0, 4), (1, 4)]
        self.map_attacking = [(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)]
        self.map = self.map_stopped
        self.walking = "walking"
        self.stopped = "stopped"
        self.shotting = "shotting"
        self.attacking = "attacking"
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
        if (self.x + self.tile_size) > self.explorer_map[1]:
            self.explorer_map[1] += self.walk_fator

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
                self.objects.add_rock(x, y, direction)

    def calculate_d(self, x, y):
        distance_x = self.x - x
        distance_y = self.y - y
        mod = self.pyxel.sqrt(distance_x**2 + distance_y**2)
        dx = distance_x / mod
        dy = distance_y / mod
        return dx, dy

    def calculate_distance(self, x, y):
        distance_x = self.x - x
        distance_y = self.y - y
        return distance_x, distance_y

    def run_ai(self, lista_enemies):
        distance_player_x, distance_player_y = self.calculate_distance(
            self.player.x, self.player.y
        )
        dx, dy = self.calculate_d(self.player.x, self.player.y)
        for enemy in lista_enemies:
            if enemy != self:
                dx_1, dy_1 = self.calculate_d(enemy.x, enemy.y)
                dx -= dx_1 / len(lista_enemies)
                dy -= dy_1 / len(lista_enemies)
        if abs(distance_player_x) > self.player.tile_size:
            self.x -= dx * self.sprint
            self.status = self.walking
            if dx > 0:
                self.flip_left()
            if dx < 0:
                self.flip_right()
        if abs(distance_player_y) > self.player.tile_size:
            self.y -= dy * self.sprint
            self.status = self.walking
        if (
            abs(distance_player_x) < self.player.tile_size
            and abs(distance_player_x) < self.player.tile_size
        ):
            self.status = self.stopped
        if distance_player_x < self.player.tile_size:
            if random.choice(range(0, 64)) == 0:
                self.status = random.choice([self.attacking, self.shotting])

    def update(self, lista_enemies):
        self.define_map()
        self.index_map = (self.index_map + 1) % (len(self.map) * self.sprint)
        self.run_ai(lista_enemies)
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
            0,
        )


class Enemies:
    def __init__(self, pyxel, tile_map, game_witht, game_height, objects, player):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.game_witht = game_witht
        self.game_height = game_height
        self.objects = objects
        self.player = player
        self.lista_Enemies = []
        self.Enemies_options = [
            Enemy_1,
        ]
        self.killed = False
        self.tick = 0

    def update(self):
        if self.tick > 120:
            self.lista_Enemies.append(
                random.choice(self.Enemies_options)(
                    self.pyxel,
                    self.tile_map,
                    self.game_witht,
                    self.game_height,
                    self.objects,
                    self.player,
                )
            )
            self.tick = 0
        else:
            self.tick += 1

        for object in self.lista_Enemies:
            object.update(self.lista_Enemies)

    def draw(self):
        for object in self.lista_Enemies:
            object.draw()
