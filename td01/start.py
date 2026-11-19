from matplotlib import pyplot as plt
import cv2

PATH_TO_IMAGE = 'imgs/'

def memo():
    #Read image as BGR image
    img = cv2.imread(PATH_TO_IMAGE + 'circles_in_a_circle.jpg')


    #Read image as grayscale image
    #version 1
    gray = cv2.imread(PATH_TO_IMAGE +  'circles_in_a_circle.jpg',cv2.IMREAD_GRAYSCALE)
    #version 2
    gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Show RGB image
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.title('my picture rgb')
    plt.show()

    #Show grayscale image
    plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
    plt.title('Gray using imread function')
    plt.show()


    plt.imshow(gray1, cmap='gray', vmin=0, vmax=255)
    plt.title('Gray using cvtColor function')
    plt.show()

    #Write image in the file
    cv2.imwrite(PATH_TO_IMAGE +  'circles_in_a_circle_gray.jpg',gray)

    #image size
    print('Image height = ', img.shape[0])
    print('Image width = ', img.shape[1])

    #Get access to a pixel
    for i in range(0,3):
        for j in range(0,3):
            pixel = img[i, j]
            print('Pixel [',i,', ',j,']= ',pixel)

    #Copy image
    img_clone = img.copy()

def exo1_invert_gray():
    img = cv2.imread(PATH_TO_IMAGE + 'lena.jpg')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255)
    plt.title('Image de base')
    plt.show()

    imgGrayInvert = imgGray.copy()

    for x in range(imgGrayInvert.shape[0]):
        for y in range(imgGrayInvert.shape[1]):
            imgGrayInvert[x][y] = 255 - imgGrayInvert[x][y]
    plt.imshow(imgGrayInvert, cmap='gray', vmin=0, vmax=255)
    plt.title("Image après transformation")
    plt.show()

    cv2.imwrite(PATH_TO_IMAGE + "exo1_result_invert_gray.jpg", imgGrayInvert)

def exo2_invert_colors():
    img = cv2.imread(PATH_TO_IMAGE + 'circles_in_a_circle.jpg')
    imgColor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(imgColor)
    plt.title("Image d'origine")
    plt.show()

    imgColorInvert = imgColor.copy()

    for x in range(imgColorInvert.shape[0]):
        for y in range(imgColorInvert.shape[1]):
            imgColorInvert[x][y][0] = 255 - imgColorInvert[x][y][0]
            imgColorInvert[x][y][1] = 255 - imgColorInvert[x][y][1]
            imgColorInvert[x][y][2] = 255 - imgColorInvert[x][y][2]

    plt.imshow(imgColorInvert)
    plt.title("Image avec couleurs inversées")
    plt.show()

    cv2.imwrite(PATH_TO_IMAGE + "exo2_result_color_invert.jpg", imgColorInvert)

def exo3_convert_rgb_to_gray():
    return

# Uncomment each exercices one by one to see results.

# exo1_invert_gray()
# exo2_invert_colors()