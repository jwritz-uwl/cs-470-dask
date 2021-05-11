import os
from skimage import data, io

io.imsave(os.path.join('images', 'image-00.png'), data.astronaut()[:256, :256, :])  # top left
io.imsave(os.path.join('images', 'image-01.png'), data.astronaut()[:256, 256:, :])  # top right
io.imsave(os.path.join('images', 'image-10.png'), data.astronaut()[256:, :256, :])  # bottom left
io.imsave(os.path.join('images', 'image-11.png'), data.astronaut()[256:, 256:, :])  # bottom right
