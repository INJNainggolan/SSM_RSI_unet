import cv2

for a in range(1, 7 ):
    image = cv2.imread('/home/zq/dataset/RSI/all/train/src/predict{0}.png'.format(a))

    print(image)

    print(image.shape)

    #####################################
    # 其他0 黑色 0 0 0 | 0 0 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 1:
                image[i][j][0] = 255
                image[i][j][1] = 255
                image[i][j][2] = 255

    #####################################
    cv2.imwrite('/home/zq/dataset/RSI/all/train/src/{0}_.png'.format(a), image[:, :])