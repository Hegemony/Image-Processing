import cv2 as cv
from cv2 import dnn

# net = dnn.readNetFromCaffe('./deploy.prototxt',
#                            './res10_300x300_ssd_iter_140000.caffemodel')


net = dnn.readNetFromCaffe('./caffe ssd model/deploy.prototxt',
                           './caffe ssd model/res10_300x300_ssd_iter_140000.caffemodel')

inWidth = 300
inHeight = 300
confThreshold = 0.8

# frame = cv.imread('./pycharmprojects/OpenCV learning/Rafd000_01_Caucasian_female_angry_frontal.jpg')
frame = cv.imread('Rafd090_21_Caucasian_male_happy_frontal.jpg')
cols = frame.shape[1]
rows = frame.shape[0]

net.setInput(dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (104.0, 177.0, 123.0), False, False))
detections = net.forward()
# perf_stats = net.getPerfProfile()
# print('Inference time, ms: %.2f' % (perf_stats[0] / cv.getTickFrequency() * 1000))
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > confThreshold:
        xLeftBottom = int(detections[0, 0, i, 3] * cols)
        yLeftBottom = int(detections[0, 0, i, 4] * rows)
        xRightTop = int(detections[0, 0, i, 5] * cols)
        yRightTop = int(detections[0, 0, i, 6] * rows)

        cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop), (0, 0, 255))

cv.imshow("detections", frame)
cv.waitKey(0)

cv.destroyAllWindows()



# blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True，crop=False,ddepth = CV_32F )
#
#    1.image，这是传入的，需要进行处理的图像。
#
#    2.scalefactor，执行完减均值后，需要缩放图像，默认是1，需要注意，scalefactor = 1 / \sigma,这是真正乘上的值。
#
#    3.size,这是神经网络，真正支持输入的值。
#
#    4.mean,这是我们要减去的均值，可以是R,G,B均值三元组，或者是一个值，每个通道都减这值。如果执行减均值，通道顺序是R、G、B。 如果，输入图像通道顺序是B、G、R，那么请确保swapRB = True，交换通道。
#
#     5.swapRB，OpenCV认为图像 通道顺序是B、G、R，而减均值时顺序是R、G、B，为了解决这个矛盾，设置swapRB=True即可。
#
#     6.crop,如果crop裁剪为真，则调整输入图像的大小，使调整大小后的一侧等于相应的尺寸，另一侧等于或大于。然后，从中心进行裁剪。如果“裁剪”为“假”，则直接调整大小而不进行裁剪并保留纵横比。
#
#     7.ddepth, 输出blob的深度，选则CV_32F or CV_8U