import cv2

def predict(use_case):
    cv2.imshow('image',use_case)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    