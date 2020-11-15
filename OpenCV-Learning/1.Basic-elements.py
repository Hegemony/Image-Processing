import cv2
# 使用cv2.imread()来读入一张图片：
# 加载灰度图
img = cv2.imread('lena.jpg', 0)
"""
参数1：图片的文件名
如果图片放在当前文件夹下，直接写文件名就行，如'lena.jpg'
否则需要给出绝对路径，如'D:\OpenCVSamples\lena.jpg'
参数2：读入方式，省略即采用默认值
cv2.IMREAD_COLOR：彩色图，默认值(1)
cv2.IMREAD_GRAYSCALE：灰度图(0)
cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
"""
cv2.imshow('lena', img)
# 参数1是窗口的名字，参数2是要显示的图片。不同窗口之间用窗口名区分，所以窗口名相同就表示是同一个窗口：
cv2.waitKey(0)
# cv2.waitKey()是让程序暂停的意思，参数是等待时间（毫秒ms）。时间一到，会继续执行接下来的程序，传入0的话表示一直等待。等待期间也可以获取用户的按键输入

# cv2.namedWindow('lena2', cv2.WINDOW_OPENGL)
# cv2.imshow('lena2', img)
# cv2.waitKey(0)

"""
使用cv2.imwrite()保存图片，参数1是包含后缀名的文件名：
"""
cv2.imwrite('lena_gray.jpg', img)