import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('TestImg.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

img.dtype, img.ndim, img.shape, img.size