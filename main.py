import pyxel

pyxel.init(320, 320)
player = pyxel.image(0)
player.load(0, 0, "player.png")

class Player():
    def __init__(self, pyxel):
        self.image = pyxel.image(0)
        self.image.load(0, 0, "images/Player-1-Stop-1.png")
        self.w = 256
        self.h = 256
    
    def flip(self):
        self.w = self.w * -1

    def draw(self):
        pyxel.blt(0, 0, self.image, 0, 0, self.w, self.h)

player = Player(pyxel)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_L):
        player.flip()

def draw():
    player.draw()

if __name__ == '__main__':
    pyxel.run(update, draw)