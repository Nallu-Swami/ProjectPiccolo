import cv2 as cv

# Load an image
img = cv.imread('download.jpg')

# Display the image in a window named "image"
cv.imshow('image', img)

# Wait for a key event and close the window
cv.waitKey(0)
cv.destroyAllWindows()