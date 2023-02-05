from flask import Flask,jsonify,Response,render_template
import project.util as util
import cv2

# URL of the IP webcam
url = "http://10.2.177.147:8080/video"


app = Flask(__name__)
app.config.from_object("project.config.Config")
app.config['UPLOAD_FOLDER'] = '../'

@app.route("/flashbang",methods= ['GET'])
def flashbang():
    util.flash_bang()
    return jsonify(success = True)

@app.route("/video",methods =['GET'])
def video():
    util.record(5)
    return jsonify(success = True)

@app.route('/video_feed')
def video_feed():
    # Open the cameras
    cap = cv2.VideoCapture(url)#

    def generate():
        while True:
            # Read a frame from the camera
            success, frame = cap.read()#

            # Encode the frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', frame)

            # Yield the frame to the generator
            yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')