import time
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO
import json

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


# 后台线程 产生数据，即刻推送至前端
def background_thread():
    count = 0
    file = open("fake.json", 'r', encoding='utf-8')
    content = file.readlines()

    for i in content:
        socketio.sleep(2)
        lists = eval(i)
        truck = 0
        suv = 0
        bus = 0
        van = 0
        pickup = 0
        sedan = 0

        for j in lists['preds']:
            if j['label'] == 'truck':
                truck += 1
            elif j['label'] == 'suv':
                suv += 1
            elif j['label'] == 'bus':
                bus += 1
            elif j['label'] == 'van':
                van += 1
            elif j['label'] == 'pickup':
                pickup += 1
            elif j['label'] == 'sedan':
                sedan += 1
        lists['truck'] = truck
        lists['suv'] = suv
        lists['bus'] = bus
        lists['van'] = van
        lists['pickup'] = pickup
        lists['sedan'] = sedan
        res = json.dumps(lists)
        socketio.emit('server_response',
                      {'data': res, 'count': count},
                      namespace='/test')
    # for i in content:
    #     res = json.dumps(i)
    #     socketio.sleep(2)
    #     count += 1
    #     t = time.strftime('%M:%S', time.localtime())
    #     # 获取系统时间（只取分:秒）
    #     socketio.emit('server_response',
    #                   {'data': res, 'count': count},
    #                   namespace='/test')
    #     # 注意：这里不需要客户端连接的上下文，默认 broadcast = True
    # for j in content:
    #     res1 = json.dumps(j)
    #     socketio.sleep(2)
    #     count += 1
    #     t = time.strftime('%M:%S', time.localtime())
    #     # 获取系统时间（只取分:秒）
    #     socketio.emit('server_response',
    #                   {'data': res1},
    #                   namespace='/test')
    #     # 注意：这里不需要客户端连接的上下文，，默认 broadcast = True


@app.route('/')
def index():
    return render_template('websocketdemo2.html', async_mode=socketio.async_mode)


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app,debug=True)
