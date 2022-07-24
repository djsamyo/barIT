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
