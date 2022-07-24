from DataMod import getContours,rotate
directory = 'Dataset/OriginalRaw'
x = 0
dir = os.listdir(directory)
dir.remove('.DS_Store')
for filename in dir:
    print('Dataset/OriginalRaw/' + filename)
    ogImage = cv2.imread('Dataset/OriginalRaw/' + filename)
    print('Dataset/OriginalRaw/' + filename[0:11] + '.png')
    maskImage = cv2.imread('Dataset/OriginalRaw/' + filename[0:11] + '.png')

    # closing all open windows
    cv2.destroyAllWindows()
    maskImage = cv2.cvtColor(maskImage, cv2.COLOR_BGR2GRAY)
    ang, x, y, w, h = getContours(maskImage)
    rotated = rotate(maskImage, ang)
    _, x, y, w, h = getContours(rotated)

    rOgImage = rotate(ogImage, ang)
    overlay = rOgImage.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 255, 255), -1)

    # Transparency factor.
    alpha = 0.8

    # Following line overlays transparent rectangle
    # over the image
    image_new = cv2.addWeighted(overlay, alpha, rOgImage, 1 - alpha, 0)

    # cropped_image = rOgImage[y:y+h, x:x+w]
    finalImg = rotate(image_new, -ang)

    cv2.imwrite('Dataset/Damaged/' + filename[0:11] + '_white.png', finalImg)
