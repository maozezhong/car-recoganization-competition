# -*- coding=utf-8 -*-
#########################################################################
# Author: mao
# Created Time: Sun May 27 17:56:47 2018
# File Name: txt2label.py
# Description: 
#        1. generate label from txt
#########################################################################

import os
import shutil

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

txt_path = '/home/maozezhong/Desktop/交通卡口车辆信息精准识别/data/train_1w_txt'
target_root_path = '/home/maozezhong/Desktop/交通卡口车辆信息精准识别/car-recoganization-competition/darknet/scripts/VOCdevkit/VOC2018/labels'
if os.path.exists(target_root_path):
    shutil.rmtree(target_root_path)
os.mkdir(target_root_path)

w, h = 1069, 500    #图像宽和高固定

for _, _, files in os.walk(txt_path):
    for file in files:
        file_path = txt_path + '/' + file

        label_path = target_root_path + '/' + file
        if os.path.exists(label_path):
            os.remove(label_path)
        out_label_file = open(label_path, 'a+')

        print(label_path)
        with open(file_path, 'r') as f:
            for line in f.readlines():
                x_min = float(line.split(' ')[1])
                x_max = float(line.split(' ')[2])
                y_min = float(line.split(' ')[3])
                y_max = float(line.split(' ')[4])
                b = (x_min, x_max, y_min, y_max)
                bb = convert((w,h), b)
                out_label_file.write(str(1) + " " + " ".join([str(a) for a in bb]) + '\n')
        
        out_label_file.close()