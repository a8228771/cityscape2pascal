#! /usr/bin/python
# -*- coding:UTF-8 -*-

# Convert cityscape dataset to pascal voc format dataset

# 2. convert '.txt' to '.xml'


import os, sys
import glob
from PIL import Image
from utils import image_id

# VEDAI 图像存储位置
src_img_dir = "/home/cessful/data_set/leftImg8bit_trainvaltest/leftImg8bit/train"
# VEDAI 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = "/home/cessful/data_set/city2pascal/Annotations/trainvaltxt"
src_xml_dir = "/home/cessful/data_set/city2pascal/Annotations/trainvalxml"

# img_Lists = glob.glob(src_img_dir + '/*.png')
img_Lists = image_id(rootdir=src_img_dir)
print(src_img_dir)
print(img_Lists)
img_basenames = []  # e.g. 100.jpg
for item in img_Lists:
    # img_basenames.append(os.path.basename(item))
    img_basenames.append(item)
    # print(item)
# print(img_basenames)
img_names = []  # e.g. 100
for item in img_basenames:
    #temp1, temp2 = os.path.splitext(item)
    img_names.append(item + '_leftImg8bit')
# print(img_names)
for img in img_names:
    im = Image.open((src_img_dir + '/' + img + '.png'))
    width, height = im.size

    # open the crospronding txt file
    gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
    # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    index = img.rfind('/')
    list_temp = list(img)
    list_temp[index] = '_'
    img_out = ''.join(list_temp)
    try:
        xml_file = open((src_xml_dir + '/' + img_out + '.xml'), 'w')
    except:
        os.mkdir(src_xml_dir)
        xml_file = open((src_xml_dir + '/' + img_out + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>CITYSCAPE</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.png' + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')

    # write the region of image on xml file
    for img_each_label in gt:
        spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
        xml_file.write('    <object>\n')
        xml_file.write('        <name>' + str(spt[0]) + '</name>\n')
        xml_file.write('        <pose>Unspecified</pose>\n')
        xml_file.write('        <truncated>0</truncated>\n')
        xml_file.write('        <difficult>0</difficult>\n')
        xml_file.write('        <bndbox>\n')
        xml_file.write('            <xmin>' + str(spt[1]) + '</xmin>\n')
        xml_file.write('            <ymin>' + str(spt[2]) + '</ymin>\n')
        xml_file.write('            <xmax>' + str(spt[3]) + '</xmax>\n')
        xml_file.write('            <ymax>' + str(spt[4]) + '</ymax>\n')
        xml_file.write('        </bndbox>\n')
        xml_file.write('    </object>\n')

    xml_file.write('</annotation>')