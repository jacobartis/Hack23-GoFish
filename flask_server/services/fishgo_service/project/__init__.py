from flask import Flask
import project.util as util
app = Flask(__name__)
app.config.from_object("project.config.Config")

@app.route("/flashbang",methods= ['GET'])
def flashbang():
    util.flash_bang()
