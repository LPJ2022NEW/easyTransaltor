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



#
# root=Window(
#     title='1'
# )
# lab=imageResiable(root,'result.jpg')
#
# root.mainloop()
