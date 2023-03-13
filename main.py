import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('TestImg.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()
#
# img.dtype, img.ndim, img.shape, img.size
img_normed = img / 127.5 - 1.0
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img)
ax[1].imshow(img_normed)
plt.show()

print("Original image:", img.mean(), img.std())
print("Normed image:", img_normed.mean(), img_normed.std())
