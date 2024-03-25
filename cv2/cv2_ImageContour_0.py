import cv2

image = cv2.imread('./yoru.jpg')
image2 = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
gray = cv2.bitwise_not(gray)

edge = cv2.Canny(gray, 100, 100)
_, thresh = cv2.threshold(edge, 127, 255, cv2.THRESH_BINARY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY, 11, 2)

thresh = cv2.erode(thresh, None, iterations = 2)
thresh = cv2.dilate(thresh, None, iterations = 2)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)

for i in range(len(sorted_contours)):
    contour = sorted_contours[i]

    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    cv2.drawContours(image, [contour], -1, (0, 255, 0), 3)
    cv2.drawContours(image2, [approx], -1, (0, 255, 0), 3)

    extLeft = tuple(contour[contour[:, :, 0].argmion()][0])
    extRight = tuple(contour[contour[:, :, 0].argmion()][0])
    extTop = tuple(contour[contour[:, :, 1].argmion()][0])
    extBot = tuple(contour[contour[:, :, 1].argmion()][0])

    cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
    cv2.circle(image, extRight, 8, (0, 0, 255), -1)
    cv2.circle(image, extTop, 8, (0, 0, 255), -1)
    cv2.circle(image, extBot, 8, (0, 0, 255), -1)

cv2.imshow('contour', image)
cv2.imshow('approx', image2)
cv2.waitKey()
cv2.destroyAllWindows()