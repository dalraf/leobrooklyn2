from PIL import Image

# Carregar imagem
im = Image.open('tile_objects.png')

# Extrair paleta de cores
palette = im.getpalette()

# Converter paleta para o formato RGB888 compatível com Pyxel
rgb_palette = []
for i in range(0, len(palette), 3):
    r, g, b = palette[i], palette[i+1], palette[i+2]
    rgb888 = (r << 16) | (g << 8) | b
    rgb_palette.append(rgb888)

# Mostrar paleta de cores compatível com Pyxel em uma lista
print(rgb_palette)

