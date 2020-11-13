from PIL import Image
import random
import os
import cv2
import shutil


# opencv图旋转,并截取
def rotate_crop(image, angle, center=None, scale=1.0, r=20):  # 1
    # 旋转，输入图像和旋转角度,r截取的半径，center中心，scale缩放
    (h, w) = image.shape[:2]  # 2
    if center is None:  # 3
        x = w / 2
        y = h / 2
        center = (x, y)  # 4 中心

    M = cv2.getRotationMatrix2D(center, angle, scale)  # 5

    rotated = cv2.warpAffine(image, M, (w, h))  # 6旋转

    a = int(x - r)  # x start
    b = int(x + r)  # x end
    c = int(y - r)  # y start
    d = int(y + r)  # y end
    cropImg = rotated[a:b, c:d]
    return cropImg  # 7


# 旋转n度，并提取中心小图
def image_rotate_crop(image_dir, save_dir, n):
    # 输入旋转角度，图像文件夹地址，保存的文件夹地址
    for f in os.listdir(image_dir):
        image_path = os.path.join(image_dir, f)
        if os.path.isfile(image_path):
            angle = 0
            im = cv2.imread(image_path)
            while angle < 360:
                re_str = str(angle) + '.jpg'
                name = f.replace('.jpg', re_str)
                save_path = os.path.join(save_dir, name)
                save_image = rotate_crop(im, angle)
                cv2.imwrite(save_path, save_image)
                angle += n


# 遍历指定目录，显示目录下的所有文件名
def CropImage4File(filepath, destpath, r):
    pathDir = os.listdir(filepath)  # list all the path or file  in filepath
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        dest = os.path.join(destpath, allDir)
        if os.path.isfile(child):
            print(child)
            image = cv2.imread(child)
            sp = image.shape  # obtain the image shape
            sz1 = sp[0]  # height(rows) of image
            sz2 = sp[1]  # width(colums) of image
            # sz3 = sp[2]#the pixels value is made up of three primary colors, here we do not use
            # 你想对文件的操作
            a = int(sz1 / 2 - r)  # x start
            b = int(sz1 / 2 + r)  # x end
            c = int(sz2 / 2 - r)  # y start
            d = int(sz2 / 2 + r)  # y end
            cropImg = image[a:b, c:d]  # crop the image
            cv2.imwrite(dest, cropImg)  # write in destination path             


# 读取文件内的所有,迭代

def read_file_all(data_dir_path, save_dir):
    for f in os.listdir(data_dir_path):
        data_file_path = os.path.join(data_dir_path, f)
        if os.path.isfile(data_file_path):
            image_rotate(data_file_path, save_dir)
            # print(collected)
        else:
            read_file_all(data_file_path)


def image_rotate(image_path, save_dir):
    # 读取图像,旋转扩充数据集
    # im = cv2.imread(image_path,0)

    im = Image.open(image_path)
    # 指定逆时针旋转的角度
    save_path = save_dir + random_name() + '.jpg'
    im.save(save_path)
    # cv2.imwrite(save_path,im)

    # im_rotate1 = im.rotate(90)
    # save_path = save_dir + random_name() + '.jpg'
    # im_rotate1.save(save_path)
    # cv2.imwrite(save_path,im_rotate1)

    # im_rotate2 = im.rotate(180)
    # save_path = save_dir + random_name() + '.jpg'
    # im_rotate2.save(save_path)

    # im_rotate3 = im.rotate(270)
    # save_path = save_dir + random_name() + '.jpg'
    # im_rotate3.save(save_path)


def random_name():
    # 随机数
    a_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
    name = random.sample(a_list, 8)
    file_name = "".join(name)
    return file_name


def image_class(image_dir, save_dir):
    # 根据文件名对图像进行分类
    for f in os.listdir(image_dir):
        image_path = os.path.join(image_dir, f)
        if os.path.isfile(image_path):
            class_name = f.split(')')[0]
            save_class_dir = save_dir + '/' + str(class_name)
            if os.path.exists(save_class_dir):
                save_class_path = os.path.join(save_class_dir, f)
                try:
                    shutil.copyfile(image_path, save_class_path)
                except:
                    pass
            else:
                os.mkdir(save_class_dir)
                save_class_path = os.path.join(save_class_dir, f)
                try:
                    shutil.copyfile(image_path, save_class_path)
                except:
                    pass


if __name__ == '__main__':
    # data_dir_path = 'E:/pcb_image_data/data_2500/test_2500/True' #读取的文件路径
    # save_dir = 'E:/pcb_image_data/data_2500_more/test_2500/True/'#保存的文件路径
    # read_file_all(data_dir_path,save_dir)

    # 截取小图
    filepath = 'E:/pcb_defect_image/class_image/Type36/True'  # source images
    destpath = 'E:/pcb_defect_image/class_image/small_image/40_40_36/True'  # resized images saved here
    CropImage4File(filepath, destpath, 20)  # 半径

    # 旋转
    # scr_dir = 'E:/pcb_image_data/2018_11_7_h/train_20/20'
    # dst_dir = 'E:/pcb_image_data/2018_11_7_h/train_20/True/'
    # read_file_all(scr_dir,dst_dir)

    # 旋转并截取小图
    # image_dir = 'E:/pcb_defect_image/2018_11_26/train/True'
    # save_dir = 'E:/pcb_defect_image/2018_11_26/image_13/train/True'

    # image_rotate_crop(image_dir, save_dir, 30)

    # 根据文件名对图片分类
    # scr_dir = 'E:/pcb_image_data/2018_11_8_h_hu/ALL/true'
    # dst_dir = 'E:/pcb_image_data/2018_11_8_h_hu/ALL/true_class'
    # image_class(scr_dir,dst_dir)

