import xmltodict
import json
import os
from utils import image_id

def json2xml(js):
    convertXml=''
    jsDict = json.load(js)
    try:
        convertXml=xmltodict.unparse(jsDict,encoding='utf-8')
    except:
        convertXml=xmltodict.unparse({'request':jsDict},encoding='utf-8')
    return convertXml
    
rootdir = '/home/cessful/data_set/leftImg8bit_trainvaltest/leftImg8bit/val'  # 写自己存放图片的数据地址
gt_dir = '/home/cessful/data_set/gtFine_trainvaltest/gtFine/val' 
names = image_id(rootdir)
for _image_id in names:
    load_f = open(gt_dir + "/%s_gtFine_polygons.json" % (_image_id), 'r')  # 导入json标签的地址
    xml = json2xml(load_f)
    out_dir = '/home/cessful/result/temp.xml'
    try:
        out_file = open(out_dir, 'w')  # 输出标签的地址
    except:
        os.makedirs(out_dir)
        out_file = open(out_dir, 'w')  # 输出标签的地址
    out_file.write(xml)
    out_file.close()