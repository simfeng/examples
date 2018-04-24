import cv2
#url = "../girl.mp4"
#url = 'rtmp://192.168.16.122:1935/rtmplive/zy'
# url = 'rtsp://admin:65535@192.168.16.252/h264/ch1/main/av_stream'
url = 'rtmp://live.hkstv.hk.lxdns.com/live/hks'
video_format = cv2.VideoWriter_fourcc(*'h264')
# video_format = cv2.VideoWriter_fourcc(*'THEO')
file_name = 'a.mp4'
camera_obj = cv2.VideoCapture(url)
# print('self.camera_obj.isOpened():', camera_obj)
frame_width, frame_height = int(camera_obj.get(3)), int(camera_obj.get(4))

out_fp = cv2.VideoWriter(file_name, video_format, 15, (frame_width, frame_height))
count = 0
while True:
    count += 1
    ret, frame = camera_obj.read()
    try:
        out_fp.write(frame)
    except Exception as e:
        print('error:', e)
    print('---- ',ret,  count)
    if count == 1000:
        break

out_fp.release()
camera_obj.release()
