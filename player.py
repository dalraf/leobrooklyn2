class Player:
    def __init__(self, pyxel):
        self.pyxel = pyxel
        self.image = self.pyxel.image(0)
        self.image.load(0, 0, "images/Player-1-Stop-1.png")
        self.w = 64
        self.h = 128
        self.x = 0
        self.y = 0
        self.walk_fator = 10

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
        self.flip_right()
        self.y -= self.walk_fator

    def walk_down(self):
        self.flip_right()
        self.y += self.walk_fator

    def draw(self):
        self.pyxel.blt(self.x, self.y, self.image, 0, 0, self.w, self.h)
