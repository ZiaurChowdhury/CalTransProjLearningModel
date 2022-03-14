# <<<<<<< HEAD
from flask import Flask, render_template, Response
import objRealTimeDectector as obj
from config import read_db_config

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
# =======
# from mysql.connector import MySQLConnection, Error
# from config import read_db_config
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
# >>>>>>> 9c6d4a331b478291cf2f1ce9e14e47a0374b3733

def connect():
    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established')
        else:
            print('Connection failed')
    
    except Error as error:
        print(error)

    return conn