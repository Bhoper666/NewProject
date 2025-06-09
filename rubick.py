import cv2
img=cv2.imread("../res/rubick.png")
cv2.namedWindow("green")
def nothing(x):
    """
    Updates the trackbars' values and applies them to the image in real time.
    """
    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lowh = cv2.getTrackbarPos( "lowh", "green")
    lows = cv2.getTrackbarPos( "lows", "green")
    lowv = cv2.getTrackbarPos( "lowv", "green")
    highh = cv2.getTrackbarPos( "highh", "green")
    highv = cv2.getTrackbarPos( "highs", "green")
    highs = cv2.getTrackbarPos( "highv", "green")
    mask = cv2.inRange(hsv , (lowh, lows, lowv), (highh, highs, highv))
    green_color=cv2.bitwise_and(img ,img,mask=mask)
    cv2.imshow("rubick", mask)
    cv2.imshow("green",green_color)
cv2.createTrackbar("lowh","green",0,255,nothing)
cv2.createTrackbar("lows","green",0,255,nothing)
cv2.createTrackbar("lowv","green",0,255,nothing)
cv2.createTrackbar("highh","green",0,255,nothing)
cv2.createTrackbar("highs","green",0,255,nothing)
cv2.createTrackbar("highv","green",0,255,nothing)
cv2.imshow("full", img)
cv2.waitKey(0)
