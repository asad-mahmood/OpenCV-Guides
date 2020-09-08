import cv2
import numpy as np

'''
Description: I am going to read in an image "Lena.jpg" using a function present in cv2
Function: imread("Path of the image")
'''
img = cv2.imread("Resources/lena.png")

'''
Description: I am now going to turn the image black and white
Function: cv2.cvtColor(img var, which color space you want to convert it too)
'''
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
Description: I am now going to turn the image blur
Function: cv2.GaussianBlur(img var, (kernel size for the blur always has to odd), sigmaX)
'''
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)

'''
Description: I am now going to try to do edge detection.
Function: cv2.Canny(img var, threshold1, threshold2)
'''
imgCanny = cv2.Canny(img, 100, 100)

'''
Description: I am now going to try to do image dilation.
Functions: 
    1. cv2.dilate(img var, kernel, iterations) Note:- Kernel is a matrix of all 1's
    2. np.ones((matrix size), defines the values in it range from 1 to 255)
'''
kernel = np.ones((5, 5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

'''
Description: I will go through the erosion function now which is the opposite of erosion
Functions: cv2.erode(img var, kernel, iterations) Note:- Kernel is a matrix of all 1's
'''
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

'''
Description: I am going to display an image using a function present in cv2.
Function: imshow("Title of the window", The variable in which you have read the image) 
'''
cv2.imshow("Gray Output", imgGray)
cv2.imshow("Blur Output", imgBlur)
cv2.imshow("Canny/Edge Detection Output", imgCanny)
cv2.imshow("Canny Image Dialated Output", imgDialation)
cv2.imshow("Dialated Image Eroded Output", imgEroded)
'''
Description: Now we have to add wait time so that image doesn't disappear.
Function: waitKey(Enter numeric amount in mili seconds)
'''
cv2.waitKey(0)  # 0 means infinite delay
