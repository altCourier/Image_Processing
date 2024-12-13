import cv2

# Capture the video on cam index 0
# Default usually 0, might be 1,2,-1 etc.
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# fourcc: video format, 20.0 fps, 640x480: width and height
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened()) # Is the cam available?
while cap.isOpened():
    ret, frame = cap.read() # Returns True if the frame is available
    # True, frame value will be saved
    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        # arguments = (source, conversion we want to do)
        gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Show frame value
        cv2.imshow('frame', gary)

        # cv2.waitKey(1) allows the program to process any keyboard events without delays.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()