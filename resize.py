
from PIL import Image
import os, sys
import glob

path = "D:\Học\Kỳ 2\\train\Xa_cu\\" #todo đường thư mục chứa ảnh
dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e = os.path.splitext(path+item)
            imResize = im.resize((150,150), Image.ANTIALIAS)
            #imResize.save(f + '', 'JPEG', quality=90)
            imResize.save('D:\Học\Kỳ 2\\train\Xa_cu2\\' + item + '', 'JPEG', quality=90) #todo đường dẫ thư mục lưu, chất lượng 90%


resize()