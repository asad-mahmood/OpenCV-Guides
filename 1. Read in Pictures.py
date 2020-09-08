import cv2

'''
Description: I am going to read in an image "Lena.jpg" using a function present in cv2
Function: imread("Path of the image")
'''
img = cv2.imread("Resources/lena.png")

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
