import imageio.v3 as iio
import os
import numpy as np
from PIL import Image

filenames = ['dog.png', 'dog1.png']
images = []
fixed_size = (300, 300)

for filename in filenames:
    if os.path.exists(filename):
        with Image.open(filename) as img:
            resized_img = img.resize(fixed_size)
            images.append(np.array(resized_img))
    else:
        print(f"File {filename} not found. Skipping...")

if images:
    iio.imwrite('dog_animation.gif', images, duration=500, loop=0)
    print("GIF created successfully as 'dog_animation.gif'")
else:
    print("No images were loaded. GIF creation aborted.")
