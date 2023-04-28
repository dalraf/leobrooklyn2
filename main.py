import pyxel

from player import Player
from objects import Objects
from event import Event
from input import Check_key
from palette import set_palette, palette

game_witht = 320
game_height = 160
tile_player = 'tile_player.png'
tile_objects = "tile_objects.png"

pyxel.init(game_witht, game_height, "Leo Broklin", 30)
set_palette(palette, tile_objects)
set_palette(palette, tile_player)

pyxel.colors.from_list(palette)

tile_map_player = pyxel.image(0)
tile_map_player.load(0, 0, tile_player)
tile_map_objects = pyxel.image(1)
tile_map_objects.load(0, 0, tile_objects)
camera = pyxel.camera
objects = Objects(
    pyxel,
    tile_map_objects,
    game_witht,
    game_height,
)
player = Player(pyxel, tile_map_player, game_witht, game_height, objects, camera)
event = Event(pyxel, player)
check_key = Check_key(pyxel, event, player)


def update():
    check_key.check_key_pressed()
    objects.update(player)


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    objects.draw()
    player.draw()


if __name__ == "__main__":
    pyxel.run(update, draw)
