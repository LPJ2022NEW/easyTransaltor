from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
import sys
import os


# 资源文件目录访问
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 访问libraries文件夹


class PaddleOcrClass:
    def __init__(self,imagPath):
        self.ocr=PaddleOCR(use_angle_cls=True, use_gpu=False)
        self.img_path= source_path(imagPath)
        self.str = ''
        self.get_text()
        self.get_img_area()

    def get_text(self):
        self.result=self.ocr.ocr(self.img_path,cls=True)
        # return self.result
    def get_img_area(self):
        self.image=Image.open(self.img_path).convert('RGB')
        self.boxes=[line[0] for line in self.result]
        # self.txts = [line[1][0] for line in self.result]
        # self.scores = [line[1][1] for line in self.result]
        # im_show = draw_ocr(self.image,self.boxes, self.txts, self.scores)
        im_show = draw_ocr(self.image, self.boxes)
        im_show = Image.fromarray(im_show)
        im_show.save('./images_saves/result.jpg')  # 结果图片保存在代码同级文件夹中。


    def get_result_line(self):
        for line in self.result:
            left_top=line[0][0]
            left_top_x=left_top[0]
            space_num=int(left_top_x//16)
            line_str=' '*space_num+line[1][0]+'\n'
            # print(' '*space_num+line[1][0])
            self.str+=line_str
        print(self.str)
        return self.str


# PaddleOcrClass('22.jpeg')