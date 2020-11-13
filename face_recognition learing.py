import face_recognition
from PIL import Image
import os


# 利用face_recognition识别数据集的人脸然后截取为128*128

def crop_face(img_path, size=(128, 128)):
    face_im = face_recognition.load_image_file(img_path)
    # 图像载入函数——load_image_file
    #        load_image_file(file, mode='RGB')
    #        加载一个图像文件到一个numpy array类型的对象上。
    #        参数：
    #        file：待加载的图像文件名字
    #        mode：转换图像的格式。只支持“RGB”(8位RGB, 3通道)和“L”(黑白)
    #        返回值：
    #        一个包含图像数据的numpy array类型的对象
    bboxs = face_recognition.face_locations(face_im)  # 自动查找图片中的所有面部
    # 人脸定位函数——face_locations
    #        face_locations(face_image,number_of_times_to_upsample=1,model="hog")
    #        利用CNN深度学习模型或方向梯度直方图（Histogram of Oriented Gradient, HOG）进行人脸提取。
    #        返回值是一个数组(top, right, bottom, left)表示人脸所在边框的四条边的位置。
    #        参数：
    #        face_image：输入的人脸图像
    #        number_of_times_to_upsample=1：从图片的样本中查找多少次人脸，该参数的值越高的话越能发现更小的人脸
    #        model="hog"：使用哪种人脸检测模型。“hog” 准确率不高，但是在CPU上运行更快，“cnn” 更准确更深度（且GPU/CUDA加速，如果有GPU支持的话），默认是“hog”
    #        返回值：
    #        一个元组列表，列表中的每个元组包含人脸的四边位置(top, right, bottom, left)
    # 批次人脸定位函数（GPU）——batch_face_locations
    #        batch_face_locations(face_images,number_of_times_to_upsample=1,batch_size=128)
    #        使用CNN人脸检测器返回一个包含人脸特征的二维数组，如果使用了GPU，这个函数能够更快速的返回结果；如果不使用GPU的话，该函数就没必要使用
    #        参数：
    #        face_images：输入多张人脸图像组成的list
    #        number_of_times_to_upsample=1：从图片的样本中查找多少次人脸，该参数的值越高的话越能发现更小的人脸
    #        batch_size=128：每个GPU一次批处理多少个image
    #        返回值：
    #        一个元组列表，列表中的每个元组包含人脸的四边位置(top, right, bottom, left)

    im = None
    if len(bboxs) > 0:
        im = Image.fromarray(face_im)  # 实现array到image的转换
        bbox = bboxs[0]
        im = im.crop((bbox[3], bbox[0], bbox[1], bbox[2]))
        # Image.crop(left, up, right, below)  左上右下
        # left：与左边界的距离
        # up：与上边界的距离
        # right：还是与左边界的距离
        # below：还是与上边界的距离

        # im.thumbnail(size, Image.ANTIALIAS)
        out = im.resize(size)  # 裁剪为128*128
        # out.save('./target/rafd-face_recognition(128-128)/' + str(count) + '.jpg', quality=95)

    return im


def file_name(file_dir):  #  单个处理
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

                i = os.path.join('./original/RaFD', i)

                face_im = face_recognition.load_image_file(i)
                bboxs = face_recognition.face_locations(face_im, model="cnn")  # 自动查找图片中的所有面部
                print(bboxs)

                im = None
                if len(bboxs) > 0:
                    im = Image.fromarray(face_im)  # 实现array到image的转换
                    print(im)
                    bbox = bboxs[0]
                    im = im.crop((bbox[3], bbox[0], bbox[1], bbox[2]))
                    # Image.crop(left, up, right, below)  左上右下
                    # left：与左边界的距离
                    # up：与上边界的距离
                    # right：还是与左边界的距离
                    # below：还是与上边界的距离

                    # im.thumbnail(size, Image.ANTIALIAS)
                    out = im.resize((128, 128))  # 裁剪为128*128
                    out.save('./target/rafd-face_recognition(128-128)/' + str(count) + '.jpg', quality=95)
                count += 1
                print(i)


# file_name('./original/RaFD')


def file_name1(file_dir):  # batch处理
    for root, dirs, files in os.walk(file_dir):

        count = 1
        cnt = 1
        list1 = []
        # 当前文件夹所有文件
        for i in files:
            # 判断是否以.jpg结尾
            if i.endswith('.jpg'):
                i = os.path.join('./original/RaFD', i)

                face_im = face_recognition.load_image_file(i)

                if cnt <= 10:
                    list1.append(face_im)
                    cnt += 1
                else:
                    bboxs = face_recognition.batch_face_locations(list1, 1, 10)  # 自动查找图片中的所有面部
                    print(bboxs)

                    im = []
                    c = 0
                    for j in list1:
                        pic = Image.fromarray(j)  # 实现array到image的转换
                        im.append(pic)
                    for k in bboxs:
                        pic1 = im[c]
                        print(pic1)

                        bbox = k[0]
                        pic1 = pic1.crop((bbox[3], bbox[0], bbox[1], bbox[2]))
                        out = pic1.resize((128, 128))  # 裁剪为128*128
                        out.save('./target/rafd-face_recognition(128-128)/' + str(count) + '.jpg', quality=95)
                        c += 1
                        count += 1
                        print(i)

                    cnt = 1
                    list1 = []



file_name1('./original/RaFD')