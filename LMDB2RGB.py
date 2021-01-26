import random
import torch
from torch.utils.data import Dataset
from torch.utils.data import sampler
import torchvision.transforms as transforms
import lmdb
import six
import sys
import bisect
import warnings
from PIL import Image
import numpy as np
import string

sys.path.append('../')
# from utils import str_filt
# from utils.labelmaps import get_vocabulary, labels2strs
from IPython import embed

random.seed(0)
import os


# train_data_dir =  [
#     '/home/notebook/data/group/branch/SR/SISR/text_dataset/zoomtxt/train1',
#     '/home/notebook/data/group/branch/SR/SISR/text_dataset/zoomtxt/train2',
#   ]

class lmdb_rgb:
    def __init__(self):
        self.train_data_dir = [
            '/home/notebook/data/group/branch/SR/SISR/text_dataset/zoomtxt/train1',
            '/home/notebook/data/group/branch/SR/SISR/text_dataset/zoomtxt/train2',
        ]
        self.output_HR_dir = './img_HR'
        self.output_lr_dir = './img_lr'
        self.output_label_dir = './label'

    def buf2PIL(self, txn, key, type='RGB'):
        imgbuf = txn.get(key)
        buf = six.BytesIO()
        buf.write(imgbuf)
        buf.seek(0)
        im = Image.open(buf).convert(type)
        return im

    def str_filt(self, str_, voc_type):
        alpha_dict = {
            'digit': string.digits,
            'lower': string.digits + string.ascii_lowercase,
            'upper': string.digits + string.ascii_letters,
            'all': string.digits + string.ascii_letters + string.punctuation
        }
        if voc_type == 'lower':
            str_ = str_.lower()
        for char in str_:
            if char not in alpha_dict[voc_type]:
                str_ = str_.replace(char, '')
        return str_

    def main(self):
        for data_dir_ in self.train_data_dir:  # 加载lmdb文件的路径
            env = lmdb.open(
                data_dir_,
                max_readers=1,
                readonly=True,
                lock=False,
                readahead=False,
                meminit=False)

            # assert index <= len(self), 'index range error'
            #     index += 1
            index = 1
            while index <= 14573:
                txn = env.begin(write=False)
                label_key = b'label-%09d' % index
                word = str(txn.get(label_key).decode())  # 用于下面做label
                img_HR_key = b'image_hr-%09d' % index  # 128*32
                img_lr_key = b'image_lr-%09d' % index  # 64*16
                # try:
                img_HR = self.buf2PIL(txn, img_HR_key, 'RGB')  # 调用上面定义的buf2PIL函数，将lmdb格式的数据转换为RGB格式
                img_lr = self.buf2PIL(txn, img_lr_key, 'RGB')
                # except IOError or len(word) > self.max_len:
                #     return [index + 1]
                label_str = self.str_filt(word, 'upper')  # 用作label
                print(img_HR, img_lr, label_str)
                img_HR.save(os.path.join(self.output_HR_dir, '{}.jpg'.format(index)))
                img_lr.save(os.path.join(self.output_lr_dir, '{}.jpg'.format(index)))

                index += 1
                # return img_HR, img_lr, label_str


lmdb_rgb().main()