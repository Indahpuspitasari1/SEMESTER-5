import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Load gambar
path = 'kkn.JPG'
image = img.imread(path)
height, width = image.shape[:2]

# Mirroring horizontal dan vertikal
horizontal = np.flip(image, axis=1)  # Flip secara horizontal
vertical = np.flip(image, axis=0)    # Flip secara vertikal
mirrored_image = np.flip(image, axis=(0, 1))  # Flip secara horizontal dan vertikal

# Tampilkan gambar asli dan hasil mirroring
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1, 4, 2)
plt.imshow(horizontal)
plt.title("Horizontal Mirror")

plt.subplot(1, 4, 3)
plt.imshow(vertical)
plt.title("Vertical Mirror")

plt.subplot(1, 4, 4)
plt.imshow(mirrored_image)
plt.title("Horizontal + Vertical Mirror")

# Simpan hasil gambar mirror
img.imwrite('mirrored_image.jpg', mirrored_image)

# Tampilkan semua gambar
plt.show()
