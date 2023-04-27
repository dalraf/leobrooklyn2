from PIL import Image

# Abre a imagem PNG
original_image = Image.open("tile_objects.png")

# Converte a imagem para o modo "P" com uma paleta de 16 cores
palette = Image.ADAPTIVE
indexed_image = original_image.convert("P", palette=palette, colors=16)

# Salva a imagem em um arquivo PNG
indexed_image.save("tile_objects.png", format="PNG")
