import cv2 as cv
import os
from utils import image_id

rootdir = '/home/cessful/data_set/leftImg8bit_trainvaltest/leftImg8bit/train'
savedir = '/home/cessful/data_set/city2pascal/JPEGImages/'

img_Lists = image_id(rootdir)
for item in img_Lists:
    full_name = rootdir + '/' + item + '_leftImg8bit' +'.png'
    img = cv.imread(full_name)
    index = item.rfind('/')
    list_temp = list(item)
    list_temp[index] = '_'
    out_path = ''.join(list_temp)
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    cv.imwrite((savedir + out_path + '.png'), img)

