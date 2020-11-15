"""
要使用摄像头，需要使用cv2.VideoCapture(0)创建VideoCapture对象，参数0指的是摄像头的编号，
如果你电脑上有两个摄像头的话，访问第2个摄像头就可以传入1，依此类推。
"""
import cv2

capture = cv2.VideoCapture(0)

while (True):
    # 获取一帧
    ret, frame = capture.read()
    # capture.read()函数返回的第1个参数ret(return value缩写)是一个布尔值，表示当前这一帧是否获取正确。
    width, height = capture.get(3), capture.get(4)
    print(width, height)
    # 将该帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # cv2.COLOR_BGR2RGB 将BGR格式转换成RGB格式
    # cv2.COLOR_BGR2GRAY 将BGR格式转换成灰度图片
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) == ord('q'):
        break

"""
播放本地视频
跟打开摄像头一样，如果把摄像头的编号换成视频的路径就可以播放本地视频了。回想一下cv2.waitKey()，它的参数表示暂停时间，
所以这个值越大，视频播放速度越慢，反之，播放速度越快，通常设置为25或30。
"""
capture = cv2.VideoCapture('demo_video.mp4')

while (capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(30) == ord('q'):
        break

"""
录制视频
之前我们保存图片用的是cv2.imwrite()，要保存视频，我们需要创建一个VideoWriter的对象，需要给它传入四个参数：

输出的文件名，如'output.avi'
编码方式FourCC码
帧率FPS
要保存的分辨率大小

FourCC是用来指定视频编码方式的四字节码，所有的编码可参考Video Codecs。
如MJPG编码可以这样写： cv2.VideoWriter_fourcc(*'MJPG')或cv2.VideoWriter_fourcc('M','J','P','G')
"""
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outfile = cv2.VideoWriter('output.avi', fourcc, 25, (640, 480))
while (capture.isOpened()):
   ret, frame = capture.read()
   if ret:
       outfile.write(frame)
       cv2.imshow('frame', frame)
       if cv2.waitKey(1) == ord('q'):
           break
   else:
       break


"""
使用cv2.VideoCapture()创建视频对象，然后在循环中一帧帧显示图像。参数传入数字时，代表打开摄像头，传入本地视频路径时，表示播放本地视频。
cap.get(propId)获取视频属性，cap.set(propId,value)设置视频属性。
cv2.VideoWriter()创建视频写入对象，用来录制/保存视频。
"""