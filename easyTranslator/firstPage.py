from ttkbootstrap import *
from easyOpeater import EasyOpeater
from translate1 import Translate_event

import pyperclip
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
#
# root = Window(
#         title="易译",
#         themename="flatly",
#         size=(300, 400),
#         resizable=(True, True),
#     )
# root.attributes('-topmost',True)
#
# firstTab(root)
# root.mainloop()