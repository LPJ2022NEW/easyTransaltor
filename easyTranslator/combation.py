import pyperclip
from pynput.mouse import Listener
import pyautogui as auto
import keyboard
import threading
from translatepy.translators.google import GoogleTranslateV2
from ttkbootstrap import *
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
import sys
import os

import pyautogui
from ttkbootstrap import *
import os
from time import sleep
from PIL import ImageGrab
# from pynput.keyboard import GlobalHotKeys
import keyboard
import sys
import os

class EasyOpeater:
    def __init__(self):
       pass
    def auto_get_clipborad(self):
        auto.hotkey('ctrl', 'c')
        text = pyperclip.paste()
        return text

    def listener(self, func):
        self.listener_mouse = Listener(on_click=func)
        self.listener_mouse.start()

    def set_hot_key_esc(self,func1):
        keyboard.add_hotkey('esc',func1)


    def set_hot_key_get_image(self,func3):
      keyboard.add_hotkey('ctrl+alt',func3)


    # def stop(self):
    #     event = threading.Event()
    #     event.set()
    #     print("stop")
    # def is_stop(self):
    #     self.set_hot_key_get_image(self.stop)



#ctrl+shift 截图键
#ctrl+alt
#ctrl+q
#esc #清空框子
# from ttkbootstrap import *
# root=Window(
#     title='1'
# )
# t=EasyOpeater()
# def fun():
#     print(1)
#
# def ff():
#     t.set_hot_key_esc(fun)
# button=Button(command=ff)
# button.pack()
# root.mainloop()

class Translate_event(GoogleTranslateV2):
    def __init__(self):
        super().__init__()
        self.translator=GoogleTranslateV2()

    def translate_to(self,data,destination_langue):
        trans = self.translator.translate(data, destination_language=destination_langue)
        return trans.result



# t=Translate_event()
# text=t.translate_to(data='你好',destination_langue='German')
# print(text)



class firstTab:
    def __init__(self,master):
        self.master=master
        self.entry_to_lange='English'
        self.show_en_lange='Chinese'


        self.translators = Translate_event()
        self.fm1=Frame(self.master)
        self.fm1.pack(side=TOP,fill=BOTH,expand=YES)

        self.fm2=Frame(self.master)
        self.fm2.pack(side=TOP,fill=BOTH,expand=YES)

        self.varContent=StringVar()

        self.initWidgets_top()
        self.initWidgets_bottom()
        self.event_active()


    def initWidgets_top(self):
        self.label_input_number = Label(self.fm1,text='输入')
        self.label_input_number.pack(side=LEFT,anchor=W,fill=BOTH,expand=YES,ipadx=5,ipady=5,padx=5,pady=5)

        self.entry = Entry(self.fm1, textvariable=self.varContent)
        self.entry.pack(side=LEFT, anchor=W,fill=BOTH,expand=YES,ipadx=5,ipady=5, padx=5,pady=5)

    def initWidgets_bottom(self):

        self.text_display = Text(self.fm2)
        self.scroll = Scrollbar(self.fm2)
        self.scroll.pack(side=RIGHT, fill='y')
        self.scroll.config(command=self.text_display.yview)
        self.text_display.config(yscrollcommand=self.scroll.set)
        self.text_display.pack(side=LEFT,anchor=W,fill=BOTH, expand=YES,padx=5,pady=5 )
        self.fm2.pack(side=TOP, fill=BOTH, expand=YES )

    def entre_text_trans(self):#获取输入结果，翻译并显示
        entry = self.varContent.get()
        reslut = self.trans_data(entry,self.entry_to_lange)#显示输入框的
        self.show_result_en_text(reslut)

    def trans_data(self, data,lange):  # 翻译#翻译鼠标中键选中的
        return self.translators.translate_to(data, lange)

    def show_result_en_text(self, result):  # 展示翻译结果
        self.text_display.delete('1.0', 'end')
        self.text_display.insert('insert', result)
        pyperclip.copy(result)  # 获取翻译内容，更加快捷操作
    def enter_show(self):#事件绑定，entry与return 即enter键绑定，将翻译结果翻译成英文
        self.entry.bind('<Return>',lambda event:self.entre_text_trans())
    # -------------------------------------------
    def is_middle_on_click(self, x, y, button, pressed):
        if pressed == 1:
            if str(button) == 'Button.middle':
                text = self.middle.auto_get_clipborad()
                # print(text)
                trans_result = self.trans_data(text,self.show_en_lange)
                self.show_result_en_text(trans_result)

    def middle_mouse(self):#对鼠标中键尽行监控
        self.middle=EasyOpeater()
        self.middle.listener(self.is_middle_on_click)
    #-----------------------------------------------------

    def mintor_keys(self):
        self.keys = EasyOpeater()
        self.keys.set_hot_key_esc(self.on_activate_esc)

    def on_activate_esc(self):
        self.varContent.set('')
        self.show_result_en_text('')
        # print(1)

    def event_active(self,*lange):
        self.middle_mouse()
        self.mintor_keys()
        self.enter_show()




class secondTab:
    def __init__(self, master):
        self.master = master
        self.text_info = '''
                __author__:          LPJ

使用说明：
1.通过用鼠标选中，通过点击鼠标中键即可得到翻译内容
2.在输入框中支持中文——>英文翻译，通过第一种方式翻译是将任何语言翻译成中文
3.快捷键设置：
	1.按esc键可以清空输入框和文本框内容
	2.按ctrl +v可以将翻译的结果粘贴下来
	3.在输入框中按enter键可以对输入框的内容进行翻译
4.对于无法选中的文字，通过打开ocr即可实现对图片文本的提取，支持多种语言
5.本软件调用各大互联网翻译厂家的官方API，实现在线翻译，翻译源可切换
6.对于ocr的提取结果可编辑，编辑之后点击翻译按钮也可得到相应结果。

        '''
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.var_3 = IntVar()
        self.lange = lange_select()
        self.lange_list = self.lange.lange_lis()

        self.frames_seting()

        self.initWidgets_second_top('entry_to')
        self.init_widget_center('test_show', 'image_ocr')
        self.initWidgets_second_bottom()

        self.set_values()
        # self.set_start_event()

    def set_values(self):
        self.com1['values'] = self.lange_list
        self.com2['values'] = self.lange_list
        self.com1.current(1)
        self.com2.current(0)
        self.com1['state'] = DISABLED
        self.com2['state'] = DISABLED

    def frames_seting(self):
        self.fm1_top = Frame(self.master)
        self.fm1_top.pack(side=TOP, fill=BOTH, expand=YES)

        self.fm2_top = Frame(self.fm1_top)
        self.fm2_top.pack(side=TOP, fill=BOTH, expand=YES)

        self.fm2_bottom = Frame(self.fm1_top)
        self.fm2_bottom.pack(side=TOP, fill=BOTH, expand=YES)
        self.fm2_checkbutton = Frame(self.fm1_top)
        self.fm2_checkbutton.pack(side=TOP, fill=BOTH, expand=YES)

        self.fm1_bottom = Frame(self.master)
        self.fm1_bottom.pack(side=TOP, fill=BOTH, expand=YES)

    def initWidgets_second_top(self, tip1):
        self.label_top = Label(self.fm2_top, text=tip1)
        self.label_top.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=5, ipady=5, padx=5, pady=5)

        self.com1 = Combobox(self.fm2_top, state='readonly')

        self.com1.pack(side=RIGHT, expand=YES)

    # ---------------------------------
    def init_widget_center(self, tip2, tip3):
        self.label_bottom = Label(self.fm2_bottom, text=tip2)
        self.label_bottom.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=5, ipady=5, padx=5, pady=5)
        self.com2 = Combobox(self.fm2_bottom, state='readonly')
        self.com2.pack(side=RIGHT, expand=YES, )

        # ---------------------------
        self.label_check = Label(self.fm2_checkbutton, text=tip3)
        self.label_check.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=5, ipady=5, padx=5, pady=5
                              )
        self.check_button = Checkbutton(self.fm2_checkbutton, textvariable=self.var_3,
                                        bootstyle="success-square-toggle")

        self.check_button.pack(anchor=W, side=RIGHT, fill=BOTH, expand=YES, ipadx=5, ipady=5, padx=5, pady=5, )

    def initWidgets_second_bottom(self):
        text_show = Text(self.fm1_bottom)
        text_show.insert(1.0, self.text_info)
        text_show.configure(state='disabled')

        text_show.pack(fill=BOTH, expand=YES, pady=5, padx=5)



    def check_com1_state(self, *args):
        self.lange.com1_select = self.com1.get()
        # self.select_1=self.lange.com1_select
        # print(self.lange.com1_select)
        # print(args)

    def check_com2_state(self, *args):
        self.lange.com2_select = self.com2.get()


class lange_select:
    def __init__(self):
        self.lange_dic()
        self.lange_lis()
        self.matinent_select()
    def lange_dic(self):
        self.dic = {
            0: 'Chinese',
            1: 'English',
            2: 'French',
            3: 'German',
            4: 'Japanese',
            5: 'Korean',
            6: 'Spanish',
            7: 'Portuguese',
            8: 'Italian'
        }
        return self.dic
    def lange_lis(self):
        self.lis=[value for value in self.dic.values()]
        return self.lis

    def matinent_select(self):
        self.com1_select=''
        self.com2_select=''




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

class DoubleText:
    def __init__(self,master,):
        self.master=Toplevel(master)

        self.x,self.y=pyautogui.size()
        self.master.geometry('{}x{}+0+0'.format(int(self.x/5),int(self.y)))
        self.master.attributes('-topmost',True)

        self.init_widgetsTop()
        self.orginTextFrame()
        self.transTextFrame()

        # self.master.mainloop()
    def init_widgetsTop(self,):
        self.frame1=Frame(self.master)
        self.frame1.pack(side=TOP,anchor=N,fill=X)

        self.topLabel=Label(self.frame1,text='当对OCR结果修改后，可按下翻译按钮翻译:')
        self.topLabel.pack(
            side=LEFT,anchor=W,fill=BOTH,expand=True
        )

        self.tranButton=Button(self.frame1,text='翻译')
        self.tranButton.pack(
            side=TOP, anchor=E, fill=BOTH,expand=True
        )

    def orginTextFrame(self):
        self.frame2=Frame(self.master)
        self.frame2.pack(side=TOP,anchor=CENTER,fill=X)
        self.orginLabel = Label(self.frame2, text='OCR识别的文本:')
        self.orginLabel.pack(
            side=TOP, anchor=N, fill=X,expand=True
        )
        self.orginText=Text(self.frame2)
        scroll = Scrollbar(self.frame2)
        # 放到窗口的右侧, 填充Y竖直方向
        scroll.pack(side=RIGHT, fill='y')

        # 两个控件关联
        scroll.config(command=self.orginText.yview)
        self.orginText.config(yscrollcommand=scroll.set)
        self.orginText.pack(side=LEFT, anchor=W, fill=BOTH, expand=YES, padx=5, pady=5)
        self.orginText.pack(side=TOP, fill=BOTH, expand=YES)
        self.orginText.pack(
            side=BOTTOM, anchor=S, fill=X,expand=True
        )

    def transTextFrame(self):
        self.frame3 = Frame(self.master)
        self.frame3.pack(side=TOP, anchor=CENTER, fill=X,expand=True)
        self.transLabel = Label(self.frame3, text='翻译后:')
        self.transLabel.pack(
            side=TOP, anchor=N, fill=X,expand=True
        )
        self.transText = Text(self.frame3)
        self.scroll1 = Scrollbar(self.frame3)
        # 放到窗口的右侧, 填充Y竖直方向
        self.scroll1.pack(side=RIGHT, fill='y')

        # 两个控件关联
        self.scroll1.config(command=self.orginText.yview)
        self.transText.config(yscrollcommand=self.scroll1.set)
        self.transText.pack(side=LEFT, anchor=W, fill=BOTH, expand=YES, padx=5, pady=5)
        self.transText.pack(side=TOP, fill=BOTH, expand=YES)
        self.transText.pack(
            side=BOTTOM, anchor=S, fill=X,expand=True
        )
        self.transText.pack(
            side=BOTTOM, anchor=S, fill=X,expand=True
        )

    def set_init_position(self):
        x,y=pyautogui.size()
        self.master.geometry('{}x{}+0+0'.format(int(x/5),int(y)))
        self.master.attributes('-topmost',True)




# 资源文件目录访问
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 访问libraries文件夹


class GetImage:
    def __init__(self,master,imageName):
        self.master=master

        self.imageName=imageName
        self.Create_folder()
        self.X=IntVar(value=0)
        self.Y=IntVar(value=0)
        self.screenWidth,self.screenHeight=pyautogui.size()

        # self.total_fin_caputre()

        # self.Create_folder()
        # self.show_top_contanier()
        # self.master.attributes('-topmost', True)
        self.sel=''


    def Create_folder(self):
        try:
            self.File_Path = os.getcwd() + "\\" + 'images_saves'
            print(self.File_Path)
            if not  os.path.exists(self.File_Path):
                os.makedirs(self.File_Path)
                print("目录新建成功：" + self.File_Path)

            else:
                print('目录已经存在！！！')

        except BaseException as msg:
            print('新建目录失败：'+msg)

    def show_top_contanier(self):
        self.top = Toplevel(self.master, width=self.screenWidth, height=self.screenHeight)
        self.top.overrideredirect(True)
        self.top.attributes('-topmost',True)
        self.canvas = Canvas(self.top, bg='white', width=self.screenWidth, height=self.screenHeight)
        self.tkimage=ImageTk.PhotoImage(self.im)
        self.canvas.create_image(self.screenWidth // 2, self.screenHeight // 2, image=self.tkimage)
        #-----------------------------------
        self.canvas.bind('<Button-1>', self.onLeftButtonDown)
        self.canvas.bind('<B1-Motion>', self.onLeftButtonMove)

        self.canvas.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        self.canvas.pack(fill=BOTH, expand=YES)

    def onLeftButtonDown(self,event):
        self.X.set(event.x)
        self.Y.set(event.y)
        #开始截图
        self.sel = True

    def onLeftButtonMove(self,event):
        if not self.sel:
            return

        global lastDraw

        try:
            self.canvas.delete(lastDraw)
        except Exception as e:
            pass

        lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')

    def onLeftButtonUp(self,event):
        self.sel = False
        try:

            self.canvas.delete(lastDraw)

        except Exception as e:

            pass
        sleep(0.1)

        left, right = sorted([self.X.get(), event.x])
        top, bottom = sorted([self.Y.get(), event.y])
        self.image = ImageGrab.grab((left + 1, top + 1, right, bottom))
        self.image.save(r'./images_saves/{}'.format(self.imageName))
        self.top.destroy()


    def start_capture_total(self):
        self.master.state('icon')
        sleep(0.15)
        self.im=ImageGrab.grab()

    def delet_temper(self):
        self.master.state('normal')

    def total_fin_caputre(self):
        self.Create_folder()
        self.start_capture_total()
        self.show_top_contanier()
        self.master.wait_window(self.top)
        self.delet_temper()
        return self.image

from ttkbootstrap import *
from PIL import Image,ImageTk
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




class imageResiable:
    def __init__(self,master,image_path):
        self.master=Toplevel(master)
        self.window_size = '300x200'

        self.master.geometry('{}+500+70'.format(self.window_size))
        self.imageFrame=Frame(self.master)
        self.imageFrame.pack(fill=BOTH,expand=YES)
        self.image_path=source_path(image_path)
        self.init_widgets()
        self.la_Resize_iamge.bind('<Configure>',self.changeSize)
        self.la_Resize_iamge.pack(fill=BOTH,expand=YES)

        #----------------------设置窗口移动事件---------------------
        self.x, self.y = 0, 0
        self.width=''
        self.height=''
        self.master.bind("<B1-Motion>", self.move)
        self.master.bind("<Button-1>", self.get_point)
        self.master.bind('<ButtonRelease-1>',self.get_new_size)

        self.master.attributes('-topmost', True)

    def init_widgets(self):
        self.la_Resize_iamge = Label(self.imageFrame)
        self.im=Image.open(self.image_path)
        self.image=ImageTk.PhotoImage(self.im)

        self.la_Resize_iamge['image']=self.image
        self.la_Resize_iamge.image=self.image

    def changeSize(self,event):
        self.width=event.width
        self.height=event.height
        self.image=ImageTk.PhotoImage(self.im.resize((event.width,event.height),Image.ANTIALIAS))
        self.la_Resize_iamge['image']=self.image
        self.la_Resize_iamge.image=self.image

    def get_point(self,event):
        self.x,self.y=event.x,event.y

    def move(self,event):
        new_x = (event.x - self.x) + self.master.winfo_x()
        new_y = (event.y - self.y) + self.master.winfo_y()
        self.window_size='{}x{}'.format(self.width,self.height)
        # print(self.window_size)
        s = f"{self.window_size}+{new_x}+{new_y}"
        # print(s)
        self.master.geometry(s)
    def get_new_size(self,event):
        pass

    def close_image(self):
        self.im.close()
        self.master.destroy()

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



#pyinstaller -F -w --clean --exclude matplotlib -p C:\Anaconda2\envs\paddleocr\Lib\shite-packages\paddleocr;C:\Anaconda2\envs\paddleocr\Lib\site-packages\paddle\libs scr2txt.py -i scr2txt.ico --add-binary C:\Anaconda2\envs\paddleocr\Lib\site-packages\paddle\libs;. --add-data C:\opencode\ocr\scr2txt\model;.\model --add-data C:\opencode\ocr\scr2txt\model\scr2txt.ico;.\ --additional-hooks-dir=.



class GuiMain:
    def __init__(self,master):
        self.master=master
        self.entry_to_lange=''
        self.show_lange=''

        self.tabs_sets()


        # self.init_songPaage()

    def tabs_sets(self):
        self.tab_str_1 = ''
        self.tab_str_2 = ''
        self.tab_str()
        self.tab = Notebook(self.master)
        self.tab_1_set()
        self.tab_2_set()
        self.tab.pack()

        self.tab.select(self.frame1)

    def tab_str(self):
        self.tab_str_1 = '                主页面             '
        self.tab_str_2 = '                设置               '

    def tab_1_set(self):
        self.frame1 = Frame(self.tab)
        self.firstaFrame=firstTab(self.frame1)
        self.tab1=self.tab.add(self.frame1,text=self.tab_str_1)


    def  tab_2_set(self):
        self.frame2 = Frame(self.tab)
        self.second = Frame(self.frame2)
        self.second.pack(
            side=TOP,
            fill=BOTH,
            expand=YES
        )
        self.secondFrame = secondTab(self.frame2)

        self.tab2 = self.tab.add(self.frame2, text=self.tab_str_2)

    def bind_change(self):
        self.secondFrame.com1.bind('<<ComboboxSelected>>',self.change_lange_show)
        self.secondFrame.com2.bind('<<ComboboxSelected>>',self.change_lang_entry)
    def change_lange_show(self):
        self.firstaFrame.show_en_lange=self.secondFrame.com1.get()
        print(self.firstaFrame.show_en_lange)
        self.firstaFrame.master.upadte()

    def change_lang_entry(self):
        self.firstaFrame.entry_to_lange=self.secondFrame.com2.get()
        print(self.firstaFrame.entry_to_lange)
        self.firstaFrame.master.upadte()

        # self.firstaFrame.enter_show(self.secondFrame.com1.get())



class GuiCombinaton:
    def __init__(self,master):
        self.master=master
        self.main_gui = GuiMain(self.master)
        self.Connect_song_page()
        self.i=0
    def Connect_song_page(self):
        self.check_open=self.main_gui.secondFrame.check_button
        self.check_open['command']=self.check_button_state
        # self.check_open['command']=self.if_button_open

        self.var_3=self.main_gui.secondFrame.var_3
        print(self.var_3)

    def check_button_state(self):

        if self.main_gui.secondFrame.var_3==0:
            self.song.songPage_close()
            self.main_gui.secondFrame.var_3=1
            if self.i == 1:
                self.main_gui.secondFrame.check_button["state"] = DISABLED
                print(9)
            print(3)

        else:
            print(4)
            self.song=songPageEvent(self.master)
            self.main_gui.secondFrame.var_3=0
            self.i=1



root = Window(
        title="易译",
        themename="flatly",
        size=(300, 400),
        resizable=(True, True),
    )
x,y=pyautogui.size()
print(x,y)
root.geometry('{}x{}+{}+{}'.format(300,400,x-300,y-500))
# print(root.size)
root.attributes('-topmost',True)
# GUI_Beat(root)
GuiCombinaton(root)
root.mainloop()


















