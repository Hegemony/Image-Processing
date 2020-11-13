from PIL import Image
import os
import cv2


# im=Image.open('test.jpg')
# out=im.resize((256,256))#
# out.save("out.jpg","JPG") #
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
        # os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
        # 在Unix，Windows中有效。
        # 语法:walk()方法语法格式如下：
        # os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
        # 参数:
        # top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
        # 遍历top给定的根目录下的所有文件夹，每个文件夹返回一个三元组(该文件夹路径，该文件夹下的文件夹名字，该文件夹下的文件名称（不包含文件夹）)
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        # topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
        # onerror -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
        # followlinks -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。
        count = 1
        # 当前文件夹所有文件
        for i in files:
            # 判断是否以.jpg结尾
            if i.endswith('.jpg'):
                # 如果是就改变图片像素为256 256
                i = os.path.join('./original/RaFD', i)
                # PIL方法
                # im = Image.open(i)
                # out = im.resize((256, 256))
                # out.save('./surprised1/' + str(count) + '.jpg', quality=95)
                # opencv方法
                im = cv2.imread(i)
                out = cv2.resize(im, (128, 128), 0, 0, cv2.INTER_LINEAR)  # 修改尺寸
                cv2.imwrite('./target/rafd(128-128)/' + str(count) + ".jpg", out, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
                # 重命名并且保存
                count += 1
                print(i)



file_name('./original/RaFD')
# 当前文件夹




# resize( InputArray src, OutputArray dst, Size dsize,
#         double fx=0, double fy=0, int interpolation=INTER_LINEAR )
# 参数解释：
# InputArray src ：输入，原图像，即待改变大小的图像；
# OutputArray dst： 输出，改变后的图像。这个图像和原图像具有相同的内容，只是大小和原图像不一样而已；
# dsize：输出图像的大小。
# 如果这个参数不为0，那么就代表将原图像缩放到这个Size(width，height)指定的大小；如果这个参数为0，那么原图像缩放之后的大小就要通过下面的公式来计算：
# dsize = Size(round(fxsrc.cols), round(fysrc.rows))
#
# 其中，fx和fy就是下面要说的两个参数，是图像width方向和height方向的缩放比例。
# fx：width方向的缩放比例，如果它是0，那么它就会按照(double)dsize.width/src.cols来计算；
# fy：height方向的缩放比例，如果它是0，那么它就会按照(double)dsize.height/src.rows来计算；
#
# interpolation：这个是指定插值的方式，图像缩放之后，肯定像素要进行重新计算的，就靠这个参数来指定重新计算像素的方式，有以下几种：
# INTER_NEAREST - 最邻近插值
# INTER_LINEAR - 双线性插值，如果最后一个参数你不指定，默认使用这种方法
# INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
# INTER_CUBIC - 4x4像素邻域内的双立方插值
# INTER_LANCZOS4 - 8x8像素邻域内的Lanczos插值
#
# # 使用函数cv2.imwrite(file，img，num)保存一个图像。第一个参数是要保存的文件名，第二个参数是要保存的图像。
#                 # 可选的第三个参数，它针对特定的格式：对于JPEG，其表示的是图像的质量，用0 - 100的整数表示，默认95;
#                 # 对于png ,第三个参数表示的是压缩级别。默认为3。
#                 # 第三个参数：
#                 # cv2.IMWRITE_JPEG_QUALITY类型为 long ,必须转换成 int
#                 # cv2.IMWRITE_PNG_COMPRESSION, 从0到9 压缩级别越高图像越小。
#                 # cv2.imwrite('1.png',img, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
#                 # cv2.imwrite('1.png',img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
