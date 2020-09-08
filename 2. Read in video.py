import cv2

'''
Description: We are going to read in a video file
Function: VideoCapture("Path of the file")
'''
cap = cv2.VideoCapture("Resources/test_video.mp4")

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
