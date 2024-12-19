# Import the OpenCV library
import cv2

# Read an image from a file
# cv2.imread(filepath, flag)
# filepath: Path to the image file
# flag: Specifies the way the image should be read
# 1 = Load a color image
# 0 = Load a grayscale image
# -1 = Load an image as is (including alpha channel)
img = cv2.imread('id.jpeg', 1)

# Display an image in a window
# cv2.imshow(window_name, image)
# window_name: Name of the window in which the image will be displayed
# image: The image to display
cv2.imshow('Image Window', img)

# Save an image to a file
# cv2.imwrite(filename, image)
# filename: Name of the file
# image: The image to save
cv2.imwrite('output_image.jpg', img)

# Convert an image to grayscale
# cv2.cvtColor(src, code)
# src: Source image
# code: Color space conversion code (e.g., cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize an image
# cv2.resize(src, dsize, fx, fy, interpolation)
# src: Source image
# dsize: Desired size of the output image (width, height)
# fx: Scale factor along the horizontal axis (0 for default)
# fy: Scale factor along the vertical axis (0 for default)
# interpolation: Interpolation method (e.g., cv2.INTER_LINEAR)
resized_img = cv2.resize(img, (800, 600))

# Draw a rectangle on an image
# cv2.rectangle(img, pt1, pt2, color, thickness)
# img: The image on which to draw
# pt1: Vertex of the rectangle
# pt2: Vertex of the opposite corner
# color: Rectangle color (B, G, R)
# thickness: Rectangle border thickness (-1 for filled rectangle)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw a circle on an image
# cv2.circle(img, center, radius, color, thickness)
# img: The image on which to draw
# center: Center of the circle (x, y)
# radius: Radius of the circle
# color: Circle color (B, G, R)
# thickness: Circle border thickness (-1 for filled circle)
cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)

# Draw a line on an image
# cv2.line(img, pt1, pt2, color, thickness)
# img: The image on which to draw
# pt1: Start point of the line
# pt2: End point of the line
# color: Line color (B, G, R)
# thickness: Line thickness
cv2.line(img, (0, 0), (250, 250), (0, 0, 255), 5)

# Add text to an image
# cv2.putText(img, text, org, font, fontScale, color, thickness, lineType)
# img: The image on which to draw
# text: The text string to be drawn
# org: Bottom-left corner of the text string in the image (x, y)
# font: Font type (e.g., cv2.FONT_HERSHEY_SIMPLEX)
# fontScale: Font scale factor
# color: Text color (B, G, R)
# thickness: Thickness of the text strokes
# lineType: Line type (optional, default is 8-connected line)
cv2.putText(img, 'Hello OpenCV', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Wait for a key event indefinitely or for a specific amount of time
# cv2.waitKey(delay)
# delay: Time in milliseconds to wait for a key event (0 = indefinitely)
cv2.waitKey(0)

# Close all OpenCV windows
# cv2.destroyAllWindows()
cv2.destroyAllWindows()