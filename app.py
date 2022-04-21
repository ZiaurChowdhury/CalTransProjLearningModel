from flask import Flask, render_template, Response
import objRealTimeDectector as obj
#flask
app = Flask(__name__)
#camera
# camera = obj.cameraCapture
#route
@app.route("/")
def index():
    #rendeing the result to HTML page
    return render_template("index.html")
@app.route("/video_feed")
def video_feed():
    #returning the video feed
    return Response(obj.videoDetector(),mimetype="multipart/x-mixed-replace; boundary=frame")
if __name__ == "__main__":
    app.run(debug=True)
