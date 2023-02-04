from flask import Flask,jsonify,Response
import project.util as util
app = Flask(__name__)
app.config.from_object("project.config.Config")

@app.route("/flashbang",methods= ['GET'])
def flashbang():
    util.flash_bang()
    return jsonify(success = True)

@app.route("/video",methods =['GET'])
def video():
    util.videoCap()
    def generate():
        with open("output.mp4", "rb") as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)
    return Response(generate(), content_type="video/mp4")
