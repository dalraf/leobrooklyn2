from PIL import Image
import os

default_colors = [
    0x000000, # preto
    0xffffff, # branco
    0xff0000, # vermelho
    0x00ff00, # verde
    0x0000ff, # azul
    0xffff00, # amarelo
    0xff00ff, # magenta
    0x00ffff, # ciano
    0x800000, # marrom
    0x808000, # oliva
    0x008000, # verde escuro
    0x008080, # azul esverdeado
    0x000080, # azul escuro
    0x800080, # roxo
    0xc0c0c0, # cinza claro
    0x808080  # cinza escuro
]

rgb_values = [value for color in default_colors for value in ((color >> 16) & 0xff, (color >> 8) & 0xff, color & 0xff)]

palette = bytes(rgb_values)

def get_palette(image):
    im = Image.open(image)
    palette = im.getpalette()
    rgb_palette = []
    for i in range(0, len(palette), 3):
        r, g, b = palette[i], palette[i + 1], palette[i + 2]
        rgb888 = (r << 16) | (g << 8) | b
        rgb_palette.append(rgb888)
    return rgb_palette


def set_palette(palette, destin):
    image_destin = Image.open(destin)
    image_destin.putpalette(palette)
    image_destin.save(destin)

def set_palette_from_orgin(origin, destin):
    reference_image = Image.open(origin)
    palette = reference_image.getpalette()
    image_destin = Image.open(destin)
    image_destin.putpalette(palette)
    image_destin.save(destin)
