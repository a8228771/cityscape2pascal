# convert cityscape dataset to pascal voc format dataset

# 1. convert every cityscape image label '.json' to '.txt'

import json
import os
from os import listdir, getcwd
from os.path import join
from utils import image_id
import os.path


# directory of Image data
rootdir = '/home/cessful/data_set/leftImg8bit_trainvaltest/leftImg8bit/train'  # 写自己存放图片的数据地址
# directory of ground truth data
gt_dir = '/home/cessful/data_set/gtFine_trainvaltest/gtFine/train'

def position(pos):
    # 该函数用来找出xmin,ymin,xmax,ymax即bbox包围框
    # This function find out xmin,ymin,xmax,ymax of a bbox
    x = []
    y = []
    nums = len(pos)
    for i in range(nums):
        x.append(pos[i][0])
        y.append(pos[i][1])
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)
    # print(x_max,y_max,x_min,y_min)
    b = (float(x_min), float(y_min), float(x_max), float(y_max))
    # print(b)
    return b

# pascal voc 标准格式
# pascal voc standard format
# < xmin > 174 < / xmin >
# < ymin > 101 < / ymin >
# < xmax > 349 < / xmax >
# < ymax > 351 < / ymax >

def convert(size, box):
    # 该函数将xmin,ymin,xmax,ymax转为x,y,w,h中心点坐标和宽高
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    print((x, y, w, h))
    return (x, y, w, h)


def convert_annotation(image_id):
    # loading .json label dir
    load_f = open(gt_dir + "/%s_gtFine_polygons.json" % (image_id), 'r')  # 导入json标签的地址
    load_dict = json.load(load_f)
    out_dir = '/home/cessful/data_set/city2pascal/Annotations/trainvaltxt/%s_leftImg8bit.txt' % (image_id)
    # output label in txt format 
    
    #################################################################
    # replace the last '/' to '_' inorder to make all file in one dir
    index = out_dir.rfind('/')
    list_temp = list(out_dir)
    list_temp[index] = '_'
    out_dir = ''.join(list_temp)
    out_file = open(out_dir, 'w')  # 输出标签的地址
    ##################################################################
    """
    try:
        out_file = open(out_dir, 'w')  # 输出标签的地址
    except: 
        index = out_dir.rfind('/')
        # os.mkdir(out_dir[:index+1])
        out_dir[index] = '_'
        out_file = open(out_dir, 'w')  # 输出标签的地址
    # keys=tuple(load_dict.keys())
    """
    w = load_dict['imgWidth']  # 原图的宽，用于归一化
    h = load_dict['imgHeight']
    # print(h)
    objects = load_dict['objects']
    nums = len(objects)
    # print(nums)
    # object_key=tuple(objects.keys()
    cls_id = ''
    for i in range(0, nums):
        labels = objects[i]['label']
        # print(i)
        # print(labels)
        pos = objects[i]['polygon']
        bb = position(pos)
        # bb = convert((w, h), b)
        cls_id = labels
        out_file.write(cls_id + " " + " ".join([str(a) for a in bb]) + '\n')
        # print(type(pos))

        if cls_id == '':
            print('no label json:',"%s_gtFine_polygons.json" % (image_id))


if __name__ == '__main__':
    names = image_id(rootdir)
    print("Image data directory: ", rootdir, "\n")
    print("Ground truth label(.json file) directory :", gt_dir, "\n")
    print("Converting...")
    for image_id in names:
        convert_annotation(image_id)
    print("done")