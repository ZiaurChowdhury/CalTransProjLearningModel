import cv2
print('This is a tool to make multiple images from video for the caltrans project from sample video')
print('Please provide me with the path to the video file you need to convert')
path = input()
vidcap = cv2.VideoCapture(path)
print('if you already used this tool give me the last number where the last image was made')
pic = input()
success,image = vidcap.read()
pic = float(pic)

start_frame_number = 0
while success:
  start_frame_number += 120
  vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
  cv2.imwrite(str(pic) + ".jpg", image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  pic +=1
