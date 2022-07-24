import numpy as np
import cv2 as cv2
import time
import os

def getContours(maskImage):
    ret, thresh = cv2.threshold(maskImage, 255, 255, 255)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x_rect, y_rect, w_rect, h_rect = cv2.boundingRect(contours[0])

    angledBox = cv2.minAreaRect(contours[0])
    (x, y), (w, h), ang = angledBox
    box = cv2.boxPoints(angledBox)
    box = np.int0(box)
    cv2.drawContours(maskImage, [box], 0, (100, 100, 100), 2)
    return (ang, x_rect, y_rect, w_rect, h_rect)


#
def rotate(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # rotate our image by 45 degrees around the center of the image
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

directory = 'Dataset/Original'
x = 0
dir = os.listdir(directory)
dir.remove('.DS_Store')
for filename in dir:
    print('Dataset/Original/'+filename)
    ogImage = cv2.imread('Dataset/Original/'+filename)
    print('Dataset/Detection/'+filename[0:11]+'.png')
    maskImage = cv2.imread('Dataset/Detection/'+filename[0:11]+'.png')

    # closing all open windows
    cv2.destroyAllWindows()
    maskImage = cv2.cvtColor(maskImage, cv2.COLOR_BGR2GRAY)
    ang, x, y, w, h = getContours(maskImage)
    rotated = rotate(maskImage, ang)
    _, x, y, w, h = getContours(rotated)

    rOgImage = rotate(ogImage, ang)
    overlay = rOgImage.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (255,255,255), -1)

    # Transparency factor.
    alpha = 0.8

    # Following line overlays transparent rectangle
    # over the image
    image_new = cv2.addWeighted(overlay, alpha, rOgImage, 1 - alpha, 0)

    # cropped_image = rOgImage[y:y+h, x:x+w]
    finalImg = rotate(image_new,-ang)

    cv2.imwrite('Dataset/UnCroppedDamage/'+filename[0:11]+'_white.png', finalImg)
