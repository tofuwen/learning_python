'第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136x640)的大小。'

import os
import glob
from PIL import Image


def change_size(path):
    for x in glob.glob('*.jpg'):
        name = os.path.join(path, x)
        im = Image.open(name)
        # not the size for iPhone 5
        im.thumbnail((100, 60))
        print(im.format, im.size, im.mode)
        im.save(name, 'JPEG')

path = '.'
change_size(path)
