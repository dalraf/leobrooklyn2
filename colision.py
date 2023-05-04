from player import Player
from rock import Rock
from enemies import Enemy_1, Enemy_2

def verify_colision(lista_all, pyxel):
    for sprite1 in lista_all:
        if isinstance(sprite1, Rock):
            for sprite2 in lista_all:
                if isinstance(sprite2, Player):
                    pyxel.quit()
