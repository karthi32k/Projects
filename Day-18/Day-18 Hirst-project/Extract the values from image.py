import colorgram

# To Extract RGB values from image
color_rgb = []
colors = colorgram.extract('image_spot.jpg', 30)

# print(colors)
# for color in colors:
#     color_rgb.append(color.rgb)
# print(color_rgb)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_rgb.append(new_color)
print(color_rgb)
