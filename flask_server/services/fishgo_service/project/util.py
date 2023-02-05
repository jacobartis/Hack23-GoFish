from playwright.sync_api import Playwright, sync_playwright

#cap = cv2.VideoCapture('https://10.2.177.147:8080/%27)
import cv2
import pathlib
import time

# URL of the IP webcam
url = "http://10.2.177.147:8080/video"

# Load the video from the URL


#Captures video for the given amount of seconds
def record(duration):
    cap = cv2.VideoCapture(url)
    #Grabs one frame from the video to calibrate the capture size
    (grabbed, frame) = cap.read()
    fshape = frame.shape
    fheight = fshape[0]
    fwidth = fshape[1]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    #Formats the video writer
    vid = cv2.VideoWriter('output.avi',fourcc, 20.0, (fwidth,fheight))

    start_time = time.time()

    while True:
        # Read the next frame from the video stream
        ret, frame = cap.read()
        # Check if the frame was successfully read
        if ret:
            vid.write(frame)
        else:
            # If there was an error reading the frame, print an error message
            print("Error: Could not read frame from the video stream.")
        if time.time()-start_time > duration:
            break
        

    # Release the video capture object
    vid.release()
    cap.release()

    # Close all the windows
    cv2.destroyAllWindows()



def flash_bang():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context().new_page()

        page.goto("http://10.2.177.147:8080/")

        button = page.query_selector("#flashbtn")
        button.click()

        browser.close()

def gen_frames():  
    camera = cv2.VideoCapture(url)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
