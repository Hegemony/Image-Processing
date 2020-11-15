"""
获取和修改像素点值
"""
import cv2

img = cv2.imread('lena.jpg')
"""
通过行列的坐标来获取某像素点的值，对于彩色图，结果是B,G,R三个值的列表，对于灰度图或单通道图，只有一个值：
"""
print(img, img.shape)  # (263, 263, 3) 行列为263，通道数为3
px = img[100, 90]  # 获取第100列，90行的图像像素值
"""
行对应y，列对应x，所以其实是img[y, x]，需要注意噢(●ˇ∀ˇ●)。容易混淆的话，可以只记行和列，行在前，列在后。
"""
print(px)  # # [103 98 197] 由于是个三通道的数，得到的是三个通道的数值

# 只获取蓝色blue通道的值 opencv默认 [B,G,R]格式进行读取 对应[0, 1, 2]
px_blue = img[100, 90, 0]
print(px_blue)  # 103

img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]
cv2.imshow('lena', img)
cv2.waitKey(0)

"""
图片属性
"""
print(img.shape)  # (263, 247, 3)
# 形状中包括行数、列数和通道数
height, width, channels = img.shape
# img是灰度图的话：height, width = img.shape
print(img.dtype)  # uint8
print(img.size)  # 263*247*3=194883

"""
ROI
ROI：Region of Interest，感兴趣区域。什么意思呢？比如我们要检测眼睛，因为眼睛肯定在脸上，所以我们感兴趣的只有脸这部分，
其他都不care，所以可以单独把脸截取出来，这样就可以大大节省计算量，提高运行速度
"""
face = img[100:200, 115:188]
"""
图片左上角的坐标是（115，100），右下角的坐标是（188，200）
"""
cv2.imshow('face', face)
cv2.waitKey(0)

"""
通道分割与合并
彩色图的BGR三个通道是可以分开单独访问的，也可以将单独的三个通道合并成一副图像。分别使用cv2.split()和cv2.merge()：
"""

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

"""
split()函数比较耗时，更高效的方式是用numpy中的索引，如提取B通道：
"""
b = img[:, :, 0]
cv2.imshow('blue', b)
cv2.waitKey(0)