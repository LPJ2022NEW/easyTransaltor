from ttkbootstrap import *
import pyautogui
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











#
# root=Window(title='1')
# DoubleText(root)
#
# root.mainloop()


