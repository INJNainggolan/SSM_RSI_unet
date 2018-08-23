import cv2

image = cv2.imread('/home/zq/dataset/RSI/all/train_building/label/1.png')

print(image)

print(image.shape)

#####################################
# 其他0 黑色 0 0 0 | 0 0 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 1:  # 植被1 RGB绿色 0 255 0
            image[i][j][0] = 0
            image[i][j][1] = 255
            image[i][j][2] = 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 2:  # 建筑2 RGB黄色 255 255 0
            image[i][j][0] = 0
            image[i][j][1] = 255
            image[i][j][2] = 255

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 3:  # 水体3 RGB蓝色 255 0 0
            image[i][j][0] = 255
            image[i][j][1] = 0
            image[i][j][2] = 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 4:  # 道路4 RGB棕色 165 42 42
            image[i][j][0] = 42
            image[i][j][1] = 42
            image[i][j][2] = 165

#####################################
cv2.imwrite('/home/zq/dataset/RSI/all/train_building/label/1_visualize.png', image[:, :])