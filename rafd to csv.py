import os
import csv
import random
import cv2
import shutil
# shutil模块提供了许多关于文件和文件集合的高级操作，特别提供了支持文件复制和删除的功能。
'''
划分数据集,随机将一个文件夹的10%的图片转移到另一个文件夹
'''

def splitdataset(srcDir, desDir):
    tempDir = srcDir
    fs = os.listdir(tempDir)  # 返回目录下里面的所有图片
    random.shuffle(fs)  # 将fs打乱
        # shuffle() 方法将序列的所有元素随机排序。
        # shuffle() 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
    le = int(len(fs)*0.9)
    for f in fs[le:]:
            # shutil.move(tempDir+'/'+f, desDir+'/'+dir + '/')
        shutil.move(tempDir + '/' + f, desDir)
# splitdataset(srcDir = './target/rafd-to-csv/train_csv', desDir = './target/rafd-to-csv/test_csv')

'''
将一个文件夹的所有文件名写入到一个文件夹下的csv文件中
'''
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # 当前文件夹所有文件
        for i in files:
            # 判断是否以.jpg结尾
            # if i.endswith('.jpg'):

            # 判断是否以.csv结尾
            if i.endswith('.csv'):
                with open('./target/rafd-to-csv/test.csv', 'a', newline='') as data_csv:
                    # writer = csv.writer(data_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                    # writer = csv.writer(data_csv, quoting=csv.QUOTE_MINIMAL) # 这种写法数据中间有空格
                    # writer.writerow(i)
                    data_csv.write(i.split('.')[0] + '.jpg ' + '\n')  # 将.csv去掉换成.jpg
                print(i)
file_name(file_dir = './target/rafd-to-csv/test_csv')