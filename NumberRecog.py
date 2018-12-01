# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
from PIL import Image
import os
from keras.models import load_model


def get_number(arr):
    index = 0
    for ele in arr[0]:
        if ele == 1:
            return index
        else:
            index = index+1

        
def Main(filename):
    col = Image.open(filename)

    model = load_model("Datas/classifier.h5")
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<115 else 255, '1')
    bw.save("result_bw.jpg")

    # Read the input image
    im = cv2.imread("result_bw.jpg")
    os.remove("result_bw.jpg")
    # Convert to grayscale and apply Gaussian filtering
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    # Threshold the image
    ret, im_th = cv2.threshold(im_gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the image
    imag, ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Get rectangles contains each contour
    rects = [cv2.boundingRect(ctr) for ctr in ctrs]

    # For each rectangular predict the number using CNN
    for rect in rects:
        # Draw the rectangles
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
        # Make the rectangular region around the digit
        leng = int(rect[3] * 1.6)
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
        roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
        # Resize the image
        roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        roi = roi.reshape(1,28,28,1)
        y_pred = model.predict(roi)
    #print(type(y_pred))
        num = get_number(y_pred)
    #print(num)
        cv2.putText(im, str(num), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

    cv2.imshow("Resulting Image with Rectangular ROIs", im)
    cv2.waitKey()

if __name__ == '__main__':
    filename = "Test_Images/1.png"
    Main(filename)