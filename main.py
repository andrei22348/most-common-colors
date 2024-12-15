import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

file_name = 'photo.jpg'
my_img = Image.open(file_name)
my_img = my_img.convert('RGB')

img_array = np.array(my_img)

plt.imshow(img_array)
plt.axis('off')
plt.show()

pixels = img_array.reshape(-1, 3)

hex_colors = ['#{:02X}{:02X}{:02X}'.format(r, g, b) for r, g, b in pixels]

hex_colors_counts = {}
for hex_color in hex_colors:
    if hex_color in hex_colors_counts:
        hex_colors_counts[hex_color] += 1
    else:
        hex_colors_counts[hex_color] = 1

sorted_by_value = sorted(hex_colors_counts.items(), key=lambda item: item[1], reverse=True)

for hex_color, count in sorted_by_value[:10]:
    percentage = (count / len(pixels)) * 100
    print(f"{hex_color}: {percentage:.5f}%")