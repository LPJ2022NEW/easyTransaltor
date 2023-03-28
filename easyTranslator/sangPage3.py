from ttkbootstrap import *
import pyautogui
from image_resize_class import imageResiable
from doubleText import DoubleText
from getImage import GetImage
from easyOpeater import EasyOpeater
from ocrClass import PaddleOcrClass
from translate1 import Translate_event
from time import sleep
import os
import sys
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class sonPageUI:  # 子页面Ui界面
    def __init__(self, master, image_path):
        self.master = master
        self.image_path = source_path(image_path)
        self.text = '请稍等几秒，ocr需要事件'
        self.start_set_GUI()

    def setImage_Frame(self, imagepath):
        self.image_show = imageResiable(self.master, source_path(imagepath))

    def setDouble_Text(self):
        self.double_text = DoubleText(self.master)
        print(1)

    def start_set_GUI(self):
        self.setImage_Frame(self.image_path)
        self.setDouble_Text()


# root = Window(
#     title='ocr'
# )


# sonPageUI(root)


class songPageEvent:
    def __init__(self, master):
        self.master = master
        self.text_wait = '请稍等几秒，ocr较慢'
        self.imagepath = source_path('./images_saves/result.jpg')

        self.start_events()
        self.text_show_wait()

    def read_and_ocr(self, imagepath):
        self.padd = PaddleOcrClass(source_path(imagepath))
        return self.padd.get_result_line()

    def text_show_wait(self):
        self.GUI.double_text.orginText.delete('1.0', 'end')
        self.GUI.double_text.orginText.insert('insert', self.text_wait)
        self.GUI.double_text.transText.delete('1.0', 'end')
        self.GUI.double_text.transText.insert('insert', self.text_wait)
    def text_delete(self):
        self.GUI.double_text.orginText.delete('1.0', 'end')
        self.GUI.double_text.transText.delete('1.0', 'end')

    def reread_image(self, path):
        self.GUI.image_show.im.close()
        self.GUI.image_show.master.destroy()
        self.GUI.setImage_Frame(path)

    def instantiation_songGUI(self):
        self.GUI = sonPageUI(self.master, self.imagepath)
        # self.reread_image()
        print(1)

    def start_events(self):
        self.instantiation_songGUI()
        self.start_ScreenCaputre()
        self.GUI.double_text.tranButton['command'] = self.editor_translator

    def start_ScreenCaputre(self):
        self.oper = EasyOpeater()
        print(1)
        self.oper.set_hot_key_get_image(self.pre_get_image)
        print(2)

    def delete_et_minimize(self):
        try:
            self.master.state('icon')
            self.GUI.image_show.close_image()
            try:
                self.GUI.double_text.master.state('icon')
            except:
                self.GUI.setDouble_Text()
                self.GUI.double_text.master.state('icon')

        except:
            pass
        sleep(0.17)
    def recover_text_build_image(self):
        self.GUI.double_text.master.state('normal')
        self.GUI.double_text.set_init_position()
        self.text_show_wait()
    def pre_get_image(self):
        self.delete_et_minimize()
        self.get_image = GetImage(self.master, '22.png')
        self.orgin_image = self.get_image.total_fin_caputre()
        print('截图完成')
        print(1)
        self.recover_text_build_image()
        self.orgin_image.save(source_path('./images_saves/22.png'))
        sleep(1)
        self.GUI.double_text.set_init_position()

        self.orgin_text=self.read_and_ocr(source_path('./images_saves/22.png'))
        self.text_delete()
        self.GUI.double_text.orginText.insert('insert',self.orgin_text)
        self.GUI.double_text.set_init_position()
        self.tran_Result()
        self.reread_image(source_path('./images_saves/result.jpg'))

    def tran_Result(self):
        self.translator = Translate_event()
        self.tran_result = self.translator.translate_to(self.orgin_text, 'Chinese')
        self.GUI.double_text.transText.delete('1.0', 'end')
        self.GUI.double_text.transText.insert('insert', self.tran_result)

    def editor_translator(self):
        self.orgin_text = self.GUI.double_text.orginText.get('1.0', 'end')
        self.GUI.double_text.transText.delete('1.0', 'end')
        self.tran_Result()

    # def songPage_close(self):
    #     # self.GUI.double_text.master.destroy()
    #     # self.GUI.image_show.master.destroy()
    #     self.master.destory()
    def songPage_close(self):
        self.GUI.double_text.master.destroy()
        self.GUI.image_show.master.destroy()


#
# songPageEvent(root)
# root.mainloop()


