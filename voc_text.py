# ----------------------------------------------------------------------#
#   验证集的划分在train.py代码里面进行
#   test.txt和val.txt里面没有内容是正常的。训练不会使用到。
# ----------------------------------------------------------------------#
import os
import random
from PIL import Image

random.seed(0)

saveBasePath = r"VOCdevkit/VisDrone2019-DET-test-dev"
folder_path = 'VOCdevkit/VOC2007/VisDrone2019-DET-test-dev/images'
namelist = []

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        namelist.append(filename)

num = len(namelist)
list = range(num)
ftest = open(os.path.join(saveBasePath, 'train.txt'), 'w')

for i in list:
    name = namelist[i][:-4] + '\n'
    ftest.write(name)

ftest.close()
