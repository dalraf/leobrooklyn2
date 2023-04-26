import pyxel

from player import Player
from event import Event
from input import Check_key

pyxel.init(960, 480)

tile_map = pyxel.image(0)
tile_map.load(0, 0, "tile_mapa.png")
player = Player(pyxel, tile_map)
event = Event(pyxel, player)
check_key = Check_key(pyxel, event, player)


def update():
    check_key.check_key_pressed()

def draw():
    player.draw()


if __name__ == "__main__":
    pyxel.run(update, draw)
