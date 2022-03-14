# # <<<<<<< HEAD
# import cv2
# import numpy as np
# def videoDetector():
#     #dnn net read yolo and coco name
#     net = cv2.dnn.readNet("./YOLO/yolov3.weights","./YOLO/yolov3.cfg")
#     #classes name
#     classes = []
#     with open("coco.names", "r") as f:
#         classes = f.read().splitlines()
#     #read video
#     # def generate_frame():
#     camera = cv2.VideoCapture(0)
#     # camera = cv2.VideoCapture('sample.mp4')
    
#     # img = cv2.imread('sample.jpg')
#     while True:
#         success,frame=camera.read()
#         if not success:
#             break
#         else:
#         #     ret,buffer=cv2.imencode('.jpg',frame)
#         #     frame=buffer.tobytes()
#         # yield(b'--frame\r\n'
#         #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#             _, img = camera.read()
#             height,width,_ = img.shape

#             #blob
#             blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), swapRB=True, crop=False)

#             #set input
#             net.setInput(blob)
#             #get output
#             output_layers = net.getUnconnectedOutLayersNames()
#             layer_outputs = net.forward(output_layers)
#             #boxes, confidences, class_ids
#             boxes = []
#             confidences = []
#             class_ids = []
#             #loop for each layer
#             for output in layer_outputs:
#                 for detection in output:
#                     scores = detection[5:]
#                     class_id = np.argmax(scores)
#                     confidence = scores[class_id]
#                     if confidence > 0.5:
#                         center_x = int(detection[0] * width)
#                         center_y = int(detection[1] * height)
#                         w = int(detection[2] * width)
#                         h = int(detection[3] * height)
#                         x = int(center_x - w / 2)
#                         y = int(center_y - h / 2)
#                         boxes.append([x, y, w, h])
#                         confidences.append(float(confidence))
#                         class_ids.append(class_id)
#             indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#             font= cv2.FONT_HERSHEY_PLAIN
#             colors = np.random.uniform(0, 255, size=(len(classes), 3))
#             for i in indexes.flatten():
#                 x,y,w,h = boxes[i]
#                 label = str(classes[class_ids[i]])
#                 confidence = str(round(confidences[i], 2))
#                 color = colors[class_ids[i]]
#                 cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#                 cv2.putText(img, label + " " + confidence, (x, y + 20), font, 1, (0,0,0), 2)
#                 ## read the camera frame
#             #show image
#             # cv2.imshow('Image',img)
#             yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg',img)[1].tobytes() + b'\r\n')
#             # key = cv2.waitKey(1)
#             # if key == 27:
#             #     break
    
#     camera.release()
#     cv2.destroyAllWindows()
# # =======
import cv2
import numpy as np


def videoDetector():
    # dnn net read yolo and coco name
    net = cv2.dnn.readNet("./YOLO/yolov3.weights", "./YOLO/yolov3.cfg")
    # classes name
    classes = []
    with open("coco.names", "r") as f:
        classes = f.read().splitlines()
    # read video
    # def generate_frame():
    camera = cv2.VideoCapture(0)
    # camera = cv2.VideoCapture('sample.mp4')

    # img = cv2.imread('sample.jpg')
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            #     ret,buffer=cv2.imencode('.jpg',frame)
            #     frame=buffer.tobytes()
            # yield(b'--frame\r\n'
            #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            _, img = camera.read()
            height, width, _ = img.shape

            # blob
            blob = cv2.dnn.blobFromImage(
                img, 1/255, (416, 416), swapRB=True, crop=False)

            # set input
            net.setInput(blob)
            # get output
            output_layers = net.getUnconnectedOutLayersNames()
            layer_outputs = net.forward(output_layers)
            #boxes, confidences, class_ids
            boxes = []
            confidences = []
            class_ids = []
            # loop for each layer
            for output in layer_outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(classes), 3))
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i], 2))
                color = colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label + " " + confidence,
                            (x, y + 20), font, 1, (0, 0, 0), 2)
                # read the camera frame
            # show image
            # cv2.imshow('Image',img)
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', img)[1].tobytes() + b'\r\n')
            # key = cv2.waitKey(1)
            # if key == 27:
            #     break

    camera.release()
    cv2.destroyAllWindows()
# >>>>>>> 9c6d4a331b478291cf2f1ce9e14e47a0374b3733
