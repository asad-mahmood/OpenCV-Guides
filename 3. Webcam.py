import cv2

'''
Description: We are going to read in a video using webcam
Functions: 
    1. VideoCapture(id of your webcam) Note:- if you have one owebcam then just write 0
    2. VideoCaptureVar.set(parameter id number, size in pixels) Note:- Enter 3 for width, 4 for height and 10 for 
        brightness
'''
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 640)
cap.set(10, 10)
'''
Description: Since our video will be read in as frames and each frame is essentially an image so we need a loop for that
 and to break out of the loop and close the frame we need to press 'q'.
Funtions:
    1. 'VideoCapture var'.read() returns a boolean variable showing success or faliure and a frame.
    2. imshow("Frame name", Frame variable) it displays the image in a frame.
    3. waitKey(delay in milliseconds) 
'''
while True:
    success, img = cap.read()
    cv2.imshow("Video Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
