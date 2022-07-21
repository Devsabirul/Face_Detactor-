import cv2
from cvzone.FaceDetectionModule import FaceDetector

cam = cv2.VideoCapture(0)
detector = FaceDetector()


while True:
    succ , img = cam.read()
    img,bBoxes = detector.findFaces(img)
    cv2.imshow("test", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()