# -*- coding=utf-8 -*-
##############################
# description:
# 将官方的csv转换为txt，每行格式如下：
# car x_min x_max y_min y_max
##############################
import pandas as pd

in_file_path = '/home/maozezhong/Desktop/交通卡口车辆信息精准识别/data/train_1w.csv'
train_data = pd.read_csv(in_file_path)
# print(train_data.head(5))
# print(train_data['coordinate'][1])

out_root_path = '/home/maozezhong/Desktop/交通卡口车辆信息精准识别/data/train_1w_txt'
for i in range(len(train_data)):
    out_file_path = out_root_path + '/' + train_data['name'][i][:-4] + '.txt'
    try:
        coords = train_data['coordinate'][i].split(';')
    except:
        print('------------warning!! ' + train_data['name'][i]+' has no coordinates!!------------')
        continue
    # print('writing '+train_data['name'][i])
    with open(out_file_path, 'w+') as f:
        for c in coords:
            #先将str转换为float，再转换为int，csv中长宽可能有小数点
            if c == '':
                print('------------coordinate is empty!------------')
                continue
            x = float(c.split('_')[0])#int(float(c.split('_')[0])) #框的左上角横坐标
            y = float(c.split('_')[1])#int(float(c.split('_')[1])) #框的左上角纵坐标
            w = float(c.split('_')[2])#int(float(c.split('_')[2])) #框的宽度
            h = float(c.split('_')[3])#int(float(c.split('_')[3])) #框的高度
            x_min = x
            x_max = x+w
            y_min = y
            y_max = y+h
            f.write('car'+' '+str(x_min)+' '+str(x_max)+' '+str(y_min)+' '+str(y_max)+'\n')
