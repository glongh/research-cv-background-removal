import cv2
import numpy as np


def trackbar_callback(self):
    pass


filename = '33-1.jpg'

img = cv2.imread(filename)  # read image
img = cv2.resize(img, (640, 480))  # resize it
img = cv2.blur(img, (3, 3))  # blur to remove noise
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR to HSV

cv2.namedWindow('Result Image (BGR)')  # window to display image

# HSV threshold
H_min = 23
H_max = 47
S_min = 100
S_max = 255
V_min = 100
V_max = 255

# Creates a trackbar to test values
cv2.createTrackbar('H_min', 'Result Image (BGR)', H_min, 255, trackbar_callback)
cv2.createTrackbar('H_max', 'Result Image (BGR)', H_max, 255, trackbar_callback)
cv2.createTrackbar('S_min', 'Result Image (BGR)', S_min, 255, trackbar_callback)
cv2.createTrackbar('S_max', 'Result Image (BGR)', S_max, 255, trackbar_callback)
cv2.createTrackbar('V_min', 'Result Image (BGR)', V_min, 255, trackbar_callback)
cv2.createTrackbar('V_max', 'Result Image (BGR)', V_max, 255, trackbar_callback)

# Should loop over a video frame by frame here
while True:
    # Read updated values from trackbar
    H_min = cv2.getTrackbarPos('H_min', 'Result Image (BGR)')
    H_max = cv2.getTrackbarPos('H_max', 'Result Image (BGR)')
    S_min = cv2.getTrackbarPos('S_min', 'Result Image (BGR)')
    S_max = cv2.getTrackbarPos('S_max', 'Result Image (BGR)')
    V_min = cv2.getTrackbarPos('V_min', 'Result Image (BGR)')
    V_max = cv2.getTrackbarPos('V_max', 'Result Image (BGR)')

    # Set mask threshold
    lower_green = np.array([H_min, S_min, V_min])
    upper_green = np.array([H_max, S_max, V_max])

    # Apply mask, get HSV image, convert to BGR
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res_hsv = cv2.bitwise_and(hsv, hsv, mask=mask)
    res_bgr = cv2.cvtColor(res_hsv, cv2.COLOR_HSV2BGR)

    # Display image
    cv2.imshow('Result Image (BGR)', res_bgr)

    # save image, use counter in case of video file
    save_file = 'extracted.jpg'
    cv2.imwrite(save_file, res_bgr)

    # Press ESC key to exit
    key = cv2.waitKey(33)
    if key == 27:
        break

# Finish
cv2.destroyAllWindows()
import numpy as np


