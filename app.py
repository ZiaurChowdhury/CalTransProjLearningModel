from flask import Flask, render_template, Response
import objRealTimeDectector as obj
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO
import json
#flask
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
#camera
# camera = obj.cameraCapture
#route
def background_thread():
    count = 0
    file = open("result.json", 'r', encoding='utf-8')
    content = file.readlines()

    for i in content:
        socketio.sleep(2)
        dicts = eval(i)
        truck = 0
        sedan = 0
        van = 0
        pickup = 0
        suv = 0
        bus = 0
        for j in dicts['preds']:
            if j['label'] == 'truck':
                truck += 1
            elif j['label'] == 'pickup':
                pickup += 1
            elif j['label'] == 'sedan':
                sedan += 1
            elif j['label'] == 'bus':
                bus += 1
            elif j['label'] == 'suv':
                suv += 1
            elif j['label'] == 'van':
                van += 1

        dicts['truck'] = truck
        dicts['pickup'] = pickup
        dicts['sedan'] = sedan
        dicts['suv'] = suv
        dicts['van'] = van
        dicts['bus'] = bus
        res = json.dumps(dicts)
        print(type(res))
        socketio.emit('server_response',
                      {'data': res, 'count': count},
                      namespace='/test')


@app.route("/")
def index():
    #rendeing the result to HTML page
    return render_template("index.html", async_mode=socketio.async_mode)
@app.route("/video_feed")
def video_feed():
    #returning the video feed
    return Response(obj.videoDetector(),mimetype="multipart/x-mixed-replace; boundary=frame")
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == "__main__":
    app.run(debug=True)
