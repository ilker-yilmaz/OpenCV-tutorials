import cv2

def resizeAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = img.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return img

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(img, dim, interpolation=inter)

    # return the resized image
    return resized

img = cv2.imread('ortakoy.jpg',1) # 0 for grayscale, 1 for color
img1 = resizeAspectRatio(img, width=400)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
cv2.imshow('Resized', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()