import csv
import os
import glob
import codecs
from PIL import Image
import os
import cv2

'''
将一个文件夹的每个csv文件的数据合并到另一个文件夹下的一个csv文件中
'''
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # 当前文件夹所有文件
        for i in files:
            # 判断是否以.csv结尾
            if i.endswith('.csv'):
                i = os.path.join(file_dir, i)
                with open('F:\\pycharmprojects\\OpenCV learning\\target\\test2\\train.csv', 'ab') as f:
                        f.write(open(i, 'rb').read())
                        # 将下面的csv内容追加到上面的csv的后面


'''
将一个文件夹的每个csv文件的数据合并到另一个文件夹下的一个txt文件中
'''
# file_name('F:\\pycharmprojects\\OpenCV learning\\target\\test1')


# csv -> txt
# import glob
#
# output_txt = 'F:\\pycharmprojects\\OpenCV learning\\target\\test2\\train.csv'
#
# for idx, f in enumerate(glob.glob('F:\\pycharmprojects\\OpenCV learning\\target\\test1\\*.csv')):
# # for idx, f in enumerate(glob.glob('./my-processed-dataset/result/*.csv')):
#     print(f)
#     with open(f, 'r') as csv_file:
#         csv_file.readline()
#         csv_list = csv_file.readline().split(', ')
#
#         if float(csv_list[1]) >= 0:
#             # print(csv_list[1])
#             aus = " ".join(csv_list[2:19])
#             # open(output_txt, 'a').write(f.split('/')[-1].split('.')[0] + '.jpg ' + aus + '\n')  #linux写法
#             # open(output_txt, 'a').write(f.split('\\')[-1].split('.')[0] + '.jpg ' + aus + '\n')  # windows写法
#             with open('F:\\pycharmprojects\\OpenCV learning\\target\\test2\\train.csv', 'a') as csv_file1:
#                 csv_file1.write(f.split('\\')[-1].split('.')[0] + '.jpg ' + aus + '\n')  # windows写法

'''
将一个文件夹的每个csv文件的第二行数据合并到另一个文件夹下的一个csv文件中
'''
import glob

output_txt = 'F:\\pycharmprojects\\OpenCV learning\\target\\test2\\train.csv'

for idx, f in enumerate(glob.glob('F:\\pycharmprojects\\OpenCV learning\\target\\test1\\*.csv')):
# for idx, f in enumerate(glob.glob('./my-processed-dataset/result/*.csv')):
    print(f)
    with open(f, 'r') as csv_file:
        csv_file.readline()
        csv_list = csv_file.readline().split(', ')
        print(csv_list)
        for i in range(0, len(csv_list)):
            csv_list[i] = csv_list[i].rstrip('\n')
        print(csv_list)

        list1 = []
        list1.append(f.split('\\')[-1].split('.')[0] + '.jpg ')
        for i in range(2, 19):
            list1.append(csv_list[i])

        with open('F:\\pycharmprojects\\OpenCV learning\\target\\test2\\train.csv', 'a', newline='') as data_csv:
            writer=csv.writer(data_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            # for data in list1:
            writer.writerow(list1)

# def data_write_csv(file_name, datas): #file_name为写入CSV文件的路径，datas为要写入数据列表
#     file_csv = codecs.open(file_name,'w+','utf-8')#追加
#     writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for data in datas:
#         writer.writerow(data)
