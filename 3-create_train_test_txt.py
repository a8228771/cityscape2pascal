# 3-create_train_test_txt.py
# encoding:utf-8

# Convert cityscape dataset to pascal voc format dataset

# 3. make train.txt/val.txt/city2pascal.txt for training and evaluation

import pdb  
import glob  
import os  
import random  
import math  

num_trainval = []
trainval_txt_list = []
category_name = ['person', 'train',
                'bicycle', 'motorbike',
                'car', 'bus']#修改类别
def get_sample_value(txt_name, category_name, _set):  
    label_path = '/home/cessful/data_set/city2pascal/Annotations/' + _set + 'txt/'  #txtfile folder
    txt_path = label_path + txt_name+'.txt'
    try:  
        with open(txt_path) as r_tdf:  
            if category_name in r_tdf.read():  
                return ' 1'  
            else:  
                return '-1'  
    except IOError as ioerr:  
        print('File error:'+str(ioerr))   
for _set in ['train', 'val', 'test']:
    

    txt_list_path = glob.glob('/home/cessful/data_set/city2pascal/Annotations/' + _set + 'txt/*.txt')
    txt_list = []
    

    for item in txt_list_path:  
        temp1,temp2 = os.path.splitext(os.path.basename(item))  
        txt_list.append(temp1)  
    txt_list.sort()  


    # 有博客建议train:val:city2pascal=8:1:1，先尝试用一下
    if (_set == 'train'):
        num_train = list(set(txt_list)) # 可修改百分比  
        num_train.sort()    
        num_trainval += num_train
        num_trainval.sort()  
    elif(_set == 'val'):
        num_val = random.sample(txt_list,int(math.floor(len(txt_list)))) # 可修改百分比  
        num_val.sort()
        num_trainval += num_val
        num_trainval.sort() 
    else:
        num_test = random.sample(txt_list,int(math.floor(len(txt_list)))) # 可修改百分比  
        num_test.sort()
            
    """
    num_val = list(set(txt_list).difference(set(num_train)))  
    num_val.sort()  
    
    #num_test = list(set(txt_list).difference(set(num_trainval)))  
    #num_test.sort()  
    #print "num_test, end = '\n\n'"
    
    # pdb.set_trace()
    """ 
    Main_path = '/home/cessful/data_set/city2pascal/ImageSets/Main/'
    Layout_path = Main_path[:-5] + 'Layout/' 
    print(Layout_path)
    if not os.path.exists(Main_path):
        os.makedirs(Main_path)
    if not os.path.exists(Layout_path):
        os.makedirs(Layout_path)
    # train_test_name = ['trainval','train','val']
    if (_set == 'train'):
        train_test_name = ['train']
    else:
        train_test_name = [_set]   

    
    # 循环写trainvl train val city2pascal
    for item_train_test_name in train_test_name:  
        list_name = 'num_'
        list_name += item_train_test_name
        train_test_txt_name = Main_path + item_train_test_name + '.txt'   
        try:  
            # 写单个文件  
            with open(train_test_txt_name, 'w') as w_tdf:  
                # 一行一行写  
                for item in eval(list_name):
                    w_tdf.write(item+'\n')  
            # 循环写Car Pedestrian Cyclist  
            for item_category_name in category_name:  
                category_txt_name = Main_path + item_category_name + '_' + item_train_test_name + '.txt'  
                with open(category_txt_name, 'w') as w_tdf:  
                    # 一行一行写  
                    for item in eval(list_name):  
                        w_tdf.write(item+' '+ get_sample_value(item, item_category_name, _set)+'\n')  
        except IOError as ioerr:  
            print('File error:'+str(ioerr))
train_test_name = 'trainval' 
list_name = 'num_'
list_name += train_test_name
train_test_txt_name = Main_path + train_test_name + '.txt' 
try:  
    # 写单个文件  
    with open(train_test_txt_name, 'w') as w_tdf:  
        # 一行一行写  
        for item in eval(list_name):
            w_tdf.write(item+'\n')  
    # 循环写Car Pedestrian Cyclist  
    for item_category_name in category_name:  
        print(item_category_name)
        category_txt_name = Main_path + item_category_name + '_' + train_test_name + '.txt'
        print(category_txt_name)  
        with open(category_txt_name, 'w') as w_tdf:  
            # 一行一行写  
            for item in eval(list_name):
                sample_value = get_sample_value(item, item_category_name, 'trainval')
                w_tdf.write(item+' '+ sample_value +'\n')  
except IOError as ioerr:  
    print('File error:'+str(ioerr)) 
