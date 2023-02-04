#cap = cv2.VideoCapture('https://10.2.177.147:8080/%27)
import cv2
import pathlib

# URL of the IP webcam
url = "http://10.2.177.147:8080/video"

# Load the video from the URL
cap = cv2.VideoCapture(url)

vid = cv2.VideoWriter(pathlib.Path().resolve(),"/test_vid.mp4")

while True:
    # Read the next frame from the video stream
    ret, frame = cap.read()
    # Check if the frame was successfully read
    if ret:
        vid.write(frame)
    else:
        # If there was an error reading the frame, print an error message
        print("Error: Could not read frame from the video stream.")

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
vid.release()
# Close all the windows
cv2.destroyAllWindows()