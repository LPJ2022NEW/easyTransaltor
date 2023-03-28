import pyautogui
from ttkbootstrap import *
import os
from time import sleep
from PIL import ImageGrab
# from pynput.keyboard import GlobalHotKeys
import keyboard
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

#
#
# root = Window(
#     title='title'
# )
# root.state('icon')
# #设置窗口大小与位置
# # def set_hot_key(func1):
# #     pass
# #     hot_key_mintor = GlobalHotKeys(
# #         {
# #             '<ctrl>+<alt>': func1,
# #
# #         })
# #     hot_key_mintor.start()
#
#
# def get_get():
#     # tt=GetImage(root,'11.png')
#     print(1)
#     tt=GetImage(root,'11.png')
#     print(2)
#     t=tt.total_fin_caputre()
#     print(3)
#
# root.geometry('100x40+400+300')
# keyboard.add_hotkey('ctrl+alt',get_get)
# # 设置窗口大小不可改变
# root.resizable(False, False)
#
#
# root.mainloop()
#
#
#
#



