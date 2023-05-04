from PIL import Image

# Load the image
image = Image.open("tile_player.png")

# Define the color to change (white in this example)
original_color_hex = "#000000"

# Define the new color to replace with (blue in this example)
new_color_hex = "#800000"

# Convert the hexadecimal color strings to RGB tuples
original_color = tuple(int(original_color_hex[i:i+2], 16) for i in (1, 3, 5))
new_color = tuple(int(new_color_hex[i:i+2], 16) for i in (1, 3, 5))

# Replace the color in the image
image_data = image.load()
for y in range(image.size[1]):
    for x in range(image.size[0]):
        if image_data[x, y] == original_color:
            image_data[x, y] = new_color

# Save the modified image
image.save("tile_player.png")
