import pyxel

from player import Player
from enemies import Enemies
from objects import Objects
from event import Event
from input import Check_key
from colision import verify_colision

game_witht = 640
game_height = 320
tile_player = "tile_player.png"
tile_objects = "tile_objects.png"

pyxel.init(game_witht, game_height, "Leo Broklin", 30)

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
enemies = Enemies(pyxel, tile_map_player, game_witht, game_height, objects, player)
event = Event(pyxel, player)
check_key = Check_key(pyxel, event, player)


def update():
    check_key.check_key_pressed()
    player.update()
    enemies.update()
    objects.update(player)
    lista_all = objects.lista_objects.copy() + enemies.lista_Enemies.copy()
    lista_all.append(player)
    verify_colision(lista_all, pyxel)

def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    pyxel.rect(
        player.camera_x,
        player.top_walking - 15 + player.tile_size,
        game_witht,
        game_height // 2,
        pyxel.COLOR_GRAY,
    )
    pyxel.rect(
        player.camera_x,
        player.top_walking + 10 + player.tile_size,
        game_witht,
        100,
        pyxel.COLOR_DARK_BLUE,
    )
    objects.draw()
    lista_sprites = enemies.lista_Enemies.copy()
    lista_sprites.append(player)
    for sprite in sorted(lista_sprites, key=lambda spr: spr.y):
        sprite.draw()

if __name__ == "__main__":
    pyxel.run(update, draw)
