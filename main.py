import cv2

def nothing(x):
    return x


cam = cv2.VideoCapture(0)

cv2.namedWindow("Video")
cv2.namedWindow("Edges")
cv2.createTrackbar("Min", "Edges", 0, 255, nothing)
cv2.createTrackbar("Max", "Edges", 0, 255, nothing)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    min_val = cv2.getTrackbarPos("Min", "Edges")
    max_val = cv2.getTrackbarPos("Max", "Edges")
    edges = cv2.Canny(gray, min_val, max_val)

    cv2.imshow("Video", frame)
    cv2.imshow("Edges", edges)
    cv2.resizeWindow("Video", 800, 600)
    cv2.resizeWindow("Edges", 800, 600)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
