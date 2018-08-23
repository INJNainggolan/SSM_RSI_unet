import cv2
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


if __name__ == '__main__':
    for a in range(1, 6):
        image = cv2.imread('/home/zq/dataset/RSI/all/train/label/{0}.png'.format(a), cv2.IMREAD_GRAYSCALE)

        print(image)

        print(image.shape)

        #####################################
        # 其他0 黑色 0 0 0 | 0 0 0

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i, j] == 1:  # 创建植被数据
                    image[i, j] = 1
                else:
                    image[i, j] = 0

#        gray = rgb2gray(image)
        #####################################
#        cv2.imwrite('/home/zq/dataset/RSI/all/train_building/label/{0}.png'.format(a), gray[:, :])
        cv2.imwrite('/home/zq/dataset/RSI/all/train_vegetation/label/{0}.png'.format(a), image[:, :])