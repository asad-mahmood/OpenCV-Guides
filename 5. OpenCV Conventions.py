import cv2
import numpy

'''
Description: I am going to read in an image "Lena.jpg" using a function present in cv2
Function: imread("Path of the image")
'''
img = cv2.imread("Resources/lambo.png")

'''
Description: I am going to display an image using a function present in cv2.
Function: imshow("Title of the window", The variable in which you have read the image) 
'''
cv2.imshow("Output", img)
'''
Description: Now we have to add wait time so that image doesn't disappear.
Function: waitKey(Enter numeric amount in mili seconds)
'''
cv2.waitKey(0)  # 0 means infinite delay

'''
Description: Now I am going to discuss the image size and how to resize, crop, tc.
Functions: 
        1. img.shape: It returns a tuple in the format of (height, width, channels) Note:- 3 in channels means BGR
        2. cv2.resize(width, height): It will resize the image to the provided pixel values
        3. img[0:height, 0:width]
'''
print(img.shape)

# Re sizing the image
imgResized = cv2.resize(img, (800, 303))
cv2.imshow("Resized Output", imgResized)
cv2.waitKey(0)  # 0 means infinite delay

# Cropping the image
imgCropped = img[0:300]
