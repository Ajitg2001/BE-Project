import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Create a function to handle button press event
def capture_image():
    # Read the current frame from the camera
    ret, frame = cap.read()

    if ret:
        # Save the frame as an image file
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured successfully!")
    else:
        print("Failed to capture image")

# Create a named window to display the captured frame
cv2.namedWindow("Camera")

while True:
    # Read the current frame from the camera
    ret, frame = cap.read()

    if ret:
        # Display the frame in the named window
        cv2.imshow("Camera", frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Check if the 'c' key is pressed (for capturing image)
    if key == ord('c'):
        capture_image()
    # Check if the 'q' key is pressed (for quitting the program)
    elif key == ord('q'):
        break

# Release the VideoCapture object and destroy the windows
cap.release()
cv2.destroyAllWindows()
