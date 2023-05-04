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
        self.x = self.player.camera_x + random.choice([0, self.game_wight])
        self.y = game_height // 2
        self.walk_fator = random.choice(range(1, 5))
        self.index_map = 0
        self.sprint = 3
        self.explorer_map = [0, game_witht]
        self.top_walking = int(game_height * 0.5)
        self.down_walking = int(game_height * 0.96) - self.tile_size
        self.left_walking = 0
        self.right_walking = game_witht
        self.map_stopped = [(0, 0)]
        self.map_walking = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
        self.map_shotting = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
        self.map_attacking = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0) ]
        self.map = self.map_stopped
        self.walking = "walking"
        self.stopped = "stopped"
        self.shotting = "shotting"
        self.attacking = "attacking"
        self.status = self.stopped
        self.old_status = self.stopped
        self.freeze_map = False
        self.killed = False
        self.life = 10

    def tile_coord(self, x, y):
        return x * self.tile_size, y * self.tile_size

    def flip_left(self):
        if self.w > 0:
            self.w *= -1

    def flip_right(self):
        if self.w < 0:
            self.w *= -1

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
                    x = self.x + int(self.tile_size * 0.25)
                if direction < 0:
                    x = self.x - int(self.tile_size * 0.25)
                y = self.y + int(self.tile_size * 0.25)
                self.objects.add_rock_enemy(x, y, direction)

    def calculate_distance_damage(self, sprite):
        distance_x = (self.x + (self.w / 2)) - (sprite.x + (sprite.w / 2))
        distance_y = (self.y + (self.h / 2)) - (sprite.y + (sprite.h / 2))
        mod = self.pyxel.sqrt(distance_x**2 + distance_y**2)
        return mod

    def calculate_distance(self, sprite):
        distance_x = self.x - sprite.x
        distance_y = self.y - sprite.y
        mod = self.pyxel.sqrt(distance_x**2 + distance_y**2)
        dx = distance_x / mod
        dy = distance_y / mod
        return abs(distance_x), abs(distance_y), dx, dy, mod

    def run_ai(self, lista_enemies):
        distance_x, distance_y, dx, dy, mod = self.calculate_distance(self.player)
        for enemy in lista_enemies:
            if enemy != self:
                _, _, dx_1, dy_1, _ = self.calculate_distance(enemy)
                dx -= dx_1 / len(lista_enemies)
                dy -= dy_1 / len(lista_enemies)
        if distance_x > self.player.tile_size:
            self.x -= dx * self.sprint
            self.status = self.walking
            if dx > 0:
                self.flip_left()
            if dx < 0:
                self.flip_right()
        if distance_y > self.player.tile_size:
            if self.y >= self.top_walking:
                self.y -= dy * self.sprint
                self.status = self.walking
            else:
                self.y = self.top_walking
        if distance_x < self.player.tile_size and distance_y < self.player.tile_size:
            self.status = self.stopped
        if distance_x < self.player.tile_size:
            if random.choice(range(0, 32)) == 0:
                self.status = self.shotting
        if mod < self.player.tile_size:
            if random.choice(range(0, 32)) == 0:
                self.status = self.attacking

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

class Enemy_2(Enemy_1):
    def __init__(self, pyxel, tile_map, game_witht, game_height, objects, player):
        super().__init__(pyxel, tile_map, game_witht, game_height, objects, player)
        self.map_stopped = [(6, 1)]
        self.map_walking = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
        self.map_shotting = [(7, 1), (0, 2), (1, 2), (2, 2), (3, 2)]
        self.map_attacking = [(7, 1), (0, 2), (1, 2), (2, 2), (3, 2)]


class Enemies:
    def __init__(self, pyxel, tile_map, game_witht, game_height, objects, player):
        self.pyxel = pyxel
        self.tile_map = tile_map
        self.game_witht = game_witht
        self.game_height = game_height
        self.objects = objects
        self.player = player
        self.lista_enemies = []
        self.enemies_options = [
            Enemy_1,
            Enemy_2
        ]
        self.killed = False

    def update(self):
        if random.choice(range(0, 128)) == 0:
            self.lista_enemies.append(
                random.choice(self.enemies_options)(
                    self.pyxel,
                    self.tile_map,
                    self.game_witht,
                    self.game_height,
                    self.objects,
                    self.player,
                )
            )

        for object in self.lista_enemies:
            object.update(self.lista_enemies)

    def draw(self):
        for object in self.lista_enemies:
            object.draw()
