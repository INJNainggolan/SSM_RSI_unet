import cv2

if __name__ == '__main__':
    for a in range(1, 7):
        image = cv2.imread('/home/zq/output/unet_output_predict/predict_building/predict{0}.png'.format(a), cv2.IMREAD_GRAYSCALE)

        print(image)

        print(image.shape)

        #####################################
        # 其他0 黑色 0 0 0 | 0 0 0

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i, j] == 1:  # 创建建筑数据
                    image[i, j] = 2
                else:
                    image[i, j] = 0

        #####################################
        cv2.imwrite('/home/zq/output/unet_output_predict/predict_mask/testing{0}_building_predict.png'.format(a), image[:, :])