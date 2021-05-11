import dask_image.imread
import dask_image.ndfilters
import dask_image.ndmeasure
import dask.array as da
import matplotlib.pyplot as plt
import os
from skimage import data, io

# converts a pixel or group of pixels to their grayscale equivalent
def pixelTransform(rgb):
    result = (rgb[..., 0])
    return result

filename_pattern = os.path.join('images', 'image-*.png')
tiled_astronaut_images = dask_image.imread.imread(filename_pattern)
result = pixelTransform(tiled_astronaut_images)

data = [[result[0, ...], result[1, ...]],
        [result[2, ...], result[3, ...]]]
combined_image = da.block(data)
print(combined_image.shape)
io.imsave(os.path.join('images', 'astronaut_red.png'), combined_image) # new image
plt.imshow(combined_image, cmap='gray')

# Display images
plt.show()
