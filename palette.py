from PIL import Image
import os


def get_palette(image):
    im = Image.open(image)
    palette = im.getpalette()
    rgb_palette = []
    for i in range(0, len(palette), 3):
        r, g, b = palette[i], palette[i + 1], palette[i + 2]
        rgb888 = (r << 16) | (g << 8) | b
        rgb_palette.append(rgb888)
    return rgb_palette


def set_palette(origin, destin):
    reference_image = Image.open(origin)
    palette = reference_image.getpalette()
    image_destin = Image.open(destin)
    image_destin.putpalette(palette)
    image_destin.save(destin)
