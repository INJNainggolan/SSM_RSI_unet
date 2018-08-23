import cv2
import numpy as np

image = cv2.imread('/home/zq/dataset/RSI/all/train_building/label/4.png', cv2.IMREAD_GRAYSCALE)
print(image)

print(image.shape)