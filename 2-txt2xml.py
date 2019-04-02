#! /usr/bin/python
# -*- coding:UTF-8 -*-

# Convert cityscape dataset to pascal voc format dataset

# 2. convert '.txt' to '.xml'


import os, sys
import glob
from PIL import Image
from utils import image_id
from xml.dom import minidom

# VEDAI 图像存储位置
src_img_dir = "/home/cessful/data_set/leftImg8bit_trainvaltest/leftImg8bit/"
# VEDAI 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = "/home/cessful/data_set/city2pascal/Annotations/"
src_xml_dir = "/home/cessful/data_set/city2pascal/Annotations/"

for _set in ['train']:
    src_txt_dir = src_txt_dir + _set + 'txt'
    src_img_dir += _set
    # img_Lists = glob.glob(src_img_dir + '/*.png')
    img_Lists = image_id(rootdir=src_img_dir)
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

        index = img.rfind('/')
        list_temp = list(img)
        list_temp[index] = '_'
        img_out = ''.join(list_temp)
        img_out = img_out[:-12]
        print(img_out)

        # open the crospronding txt file
        gt = open(src_txt_dir + '/' + img_out + '.txt').read().splitlines()
        # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

        # write in xml file
        # modified 2019-4-1 using xml mindom
        impl = minidom.getDOMImplementation()

        # create a xml dom
        # param: namespaceURI, qualifiedName, doctype
        doc = impl.createDocument(None, None, None)

        # creating root element
        rootElement = doc.createElement('annotation')
        
        folderElement = doc.createElement('folder')
        folderScriptText = doc.createTextNode('CITYSCAPE')
        folderElement.appendChild(folderScriptText)
        rootElement.appendChild(folderElement)

        filenameElement = doc.createElement('filename')
        filenameScriptText = doc.createTextNode(img_out + '.jpg')
        filenameElement.appendChild(filenameScriptText)
        rootElement.appendChild(filenameElement)

        sourceElement = doc.createElement('source')
        
        databaseElement = doc.createElement('database')
        databaseScriptText = doc.createTextNode('The CITYSCAPE Database')
        databaseElement.appendChild(databaseScriptText)
        annotationElement = doc.createElement('annotation')
        annotationScriptText = doc.createTextNode('CITYSCAPE Database')
        annotationElement.appendChild(annotationScriptText)
        imageElement = doc.createElement('image')
        imageScriptText = doc.createTextNode('flickr')
        imageElement.appendChild(imageScriptText)
        flickridElement = doc.createElement('flickrid')
        flickridScriptText = doc.createTextNode('0')
        flickridElement.appendChild(flickridScriptText)

        sourceElement.appendChild(databaseElement)
        sourceElement.appendChild(annotationElement)
        sourceElement.appendChild(imageElement)
        sourceElement.appendChild(flickridElement)
        rootElement.appendChild(sourceElement)

        ownerElement = doc.createElement('owner')
        
        flickridElement2 = doc.createElement('flickrid')
        flickridScriptText2 = doc.createTextNode('cityscape team')
        flickridElement2.appendChild(flickridScriptText2)
        nameElement = doc.createElement('name')
        nameScriptText = doc.createTextNode('cessfulshen reconstruct')
        nameElement.appendChild(nameScriptText)

        ownerElement.appendChild(flickridElement2)
        ownerElement.appendChild(nameElement)
        rootElement.appendChild(ownerElement)

        sizeElement = doc.createElement('size')

        widthElement = doc.createElement('width')
        widthScriptText = doc.createTextNode(str(width))
        widthElement.appendChild(widthScriptText)
        heightElement = doc.createElement('height')
        heightScriptText = doc.createTextNode(str(height))
        heightElement.appendChild(heightScriptText)
        depthElement = doc.createElement('depth')
        depthScriptText = doc.createTextNode('3')
        depthElement.appendChild(depthScriptText)

        sizeElement.appendChild(widthElement)
        sizeElement.appendChild(heightElement)
        sizeElement.appendChild(depthElement)
        rootElement.appendChild(sizeElement)

        segmentedElement = doc.createElement('segmented')
        segmentedScriptText = doc.createTextNode('0')
        segmentedElement.appendChild(segmentedScriptText)
        rootElement.appendChild(segmentedElement)

        for img_each_label in gt:
            spt = img_each_label.split(',')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
            objectE = doc.createElement('object')

            nameE = doc.createElement('name')
            nameSText = doc.createTextNode(spt[0])
            nameE.appendChild(nameSText)
            poseE = doc.createElement('pose')
            poseSText = doc.createTextNode('Unspecified')
            poseE.appendChild(poseSText)
            truncatedE = doc.createElement('truncated')
            truncatedSText = doc.createTextNode('0')
            truncatedE.appendChild(truncatedSText)
            difficultE = doc.createElement('difficult')
            difficultSText = doc.createTextNode('0')
            difficultE.appendChild(difficultSText)
            bndboxE = doc.createElement('bndbox')
            
            xminE = doc.createElement('xmin')
            xminSText = doc.createTextNode(str(int(round(float(spt[1])+1))))
            xminE.appendChild(xminSText)
            yminE = doc.createElement('ymin')
            yminSText = doc.createTextNode(str(int(round(float(spt[2])+1))))
            yminE.appendChild(yminSText)
            xmaxE = doc.createElement('xmax')
            xmaxSText = doc.createTextNode(str(int(round(float(spt[3])+1))))
            xmaxE.appendChild(xmaxSText)
            ymaxE = doc.createElement('ymax')
            ymaxSText = doc.createTextNode(str(int(round(float(spt[4])+1))))
            ymaxE.appendChild(ymaxSText)

            bndboxE.appendChild(xminE)
            bndboxE.appendChild(yminE)
            bndboxE.appendChild(xmaxE)
            bndboxE.appendChild(ymaxE)

            objectE.appendChild(nameE)
            objectE.appendChild(poseE)
            objectE.appendChild(truncatedE)
            objectE.appendChild(difficultE)
            objectE.appendChild(bndboxE)
            rootElement.appendChild(objectE)
       
        doc.appendChild(rootElement)

        try:
            xml_file = open((src_xml_dir + '/' + img_out + '.xml'), 'w')
        except:
            os.mkdir(src_xml_dir)
            xml_file = open((src_xml_dir + '/' + img_out + '.xml'), 'w')
        doc.writexml(xml_file, addindent='\t', newl='\n')
        xml_file.close()

        """
        # os.mknod(src_xml_dir + '/' + img + '.xml')
        try:
            xml_file = open((src_xml_dir + '/' + img_out + '.xml'), 'w')
        except:
            os.mkdir(src_xml_dir)
            xml_file = open((src_xml_dir + '/' + img_out + '.xml'), 'w')
        xml_file.write('<annotation>\n')
        xml_file.write('    <folder>CITYSCAPE</folder>\n')
        xml_file.write('    <filename>' + str(img_out) + '.jpg' + '</filename>\n')
        xml_file.write('    <size>\n')
        xml_file.write('        <width>' + str(width) + '</width>\n')
        xml_file.write('        <height>' + str(height) + '</height>\n')
        xml_file.write('        <depth>3</depth>\n')
        xml_file.write('    </size>\n')

        # write the region of image on xml file
        for img_each_label in gt:
            spt = img_each_label.split(',')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
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
        """