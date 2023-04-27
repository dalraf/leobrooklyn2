import pyxel

from player import Player
from objects import Objects
from event import Event
from input import Check_key

pyxel.init(320, 160, 'Leo Broklin', 30)

tile_map_player = pyxel.image(0)
tile_map_player.load(0, 0, "tile_player.png")
tile_map_objects = pyxel.image(1)
tile_map_objects.load(0, 0, "tile_objects.png")

objects = Objects(pyxel, tile_map_objects)
player = Player(pyxel, tile_map_player, objects)
event = Event(pyxel, player)
check_key = Check_key(pyxel, event, player)


def update():
    check_key.check_key_pressed()

def draw():
    pyxel.cls(0)
    player.draw()
    objects.draw()


if __name__ == "__main__":
    pyxel.run(update, draw)
