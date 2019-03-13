# Cityscape 2 Pascal VOC
convert cityscape bbox label formatto pascal voc bbox label format
## Pascal VOC dataset file Structure
```.
└── VOCdevkit     #根目录
    └── VOC2012   #不同年份的数据集，这里只下载了2012的，还有2007等其它年份的
        ├── Annotations        #存放xml文件，与JPEGImages中的图片一一对应，解释图片的内容等等
        ├── ImageSets          #该目录下存放的都是txt文件，txt文件中每一行包含一个图片的名称，末尾会加上±1表示正负样本
        │   ├── Action
        │   ├── Layout
        │   ├── Main
        │   └── Segmentation
        ├── JPEGImages         #存放源图片
        ├── SegmentationClass  #存放的是图片，分割后的效果，见下文的例子
        └── SegmentationObject #存放的是图片，分割后的效果，见下文的例子
``` 
from：https://blog.csdn.net/u013832707/article/details/80060327 
 

#### This repository is forcked from https://github.com/tianyolanda/cityscape2pascal
