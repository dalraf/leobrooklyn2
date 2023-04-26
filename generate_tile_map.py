from PIL import Image
import os
import pyxel

# Define as configurações do mapa
tile_size = 64
map_width = 10
map_height = 15

# Define o diretório onde estão as imagens
dir_path = "./images/"

# Abre todas as imagens e as adiciona ao arquivo do mapa
map_image = Image.new("RGBA", (tile_size*map_width, tile_size*map_height), (0, 0, 0, 0))
for i, file_name in enumerate(sorted(os.listdir(dir_path))):
    if file_name.endswith(".png"):
        tile_image = Image.open(os.path.join(dir_path, file_name)).convert("RGBA")
        tile_image = tile_image.resize((tile_size, tile_size))
        x = i % map_width
        y = i // map_width
        map_image.paste(tile_image, (x*tile_size, y*tile_size))

# Salva o arquivo do mapa
map_image.save("tile_mapa.png")





