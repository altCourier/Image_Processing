# Import OpenCV
import cv2

# Read the image
img = cv2.imread("assets/image.png", -1)

# Show the image
cv2.imshow('Image', img)

# Wait infitine amount of times for input
# If it was 5, wait 5 secs 
k = cv2.waitKey(0) & 0xFF # For 64 bit machines it is better to add & 0xFF

if k == 27: # 27 == <Escape>
    # Destory all windows so they don't loiter background
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('image_copy.png', img)
    cv2.destroyAllWindows()


