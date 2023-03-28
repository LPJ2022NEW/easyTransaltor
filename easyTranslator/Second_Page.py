from ttkbootstrap import *
from translate1 import Translate_event
from lange_seting import lange_select

class secondTab:
    def __init__(self,master):
        self.master=master
        self.text_info='''
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
        self.lange=lange_select()
        self.lange_list=self.lange.lange_lis()

        self.frames_seting()

        self.initWidgets_second_top('entry_to')
        self.init_widget_center('test_show','image_ocr')
        self.initWidgets_second_bottom()

        self.set_values()
        # self.set_start_event()

    def set_values(self):
        self.com1['values'] = self.lange_list
        self.com2['values'] = self.lange_list
        self.com1.current(1)
        self.com2.current(0)
        self.com1['state']=DISABLED
        self.com2['state']=DISABLED







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

    def initWidgets_second_top(self,tip1):
        self.label_top = Label(self.fm2_top, text=tip1 )
        self.label_top.pack( side=LEFT,fill=BOTH,   expand=YES, ipadx=5,  ipady=5, padx=5,  pady=5)

        self.com1 = Combobox( self.fm2_top, state='readonly')

        self.com1.pack(side=RIGHT,  expand=YES)
#---------------------------------
    def init_widget_center(self,tip2,tip3):
        self.label_bottom = Label(self.fm2_bottom, text=tip2)
        self.label_bottom.pack( side=LEFT, fill=BOTH, expand=YES,  ipadx=5,  ipady=5,  padx=5,  pady=5 )
        self.com2 = Combobox(self.fm2_bottom,state='readonly')
        self.com2.pack(  side=RIGHT, expand=YES,)

        #---------------------------
        self.label_check = Label(self.fm2_checkbutton,  text=tip3)
        self.label_check.pack( side=LEFT,fill=BOTH,expand=YES,ipadx=5,ipady=5,padx=5,pady=5
        )
        self.check_button=Checkbutton(self.fm2_checkbutton,textvariable=self.var_3,bootstyle="success-square-toggle")

        self.check_button.pack( anchor=W,side=RIGHT,fill=BOTH,expand=YES,ipadx=5,ipady=5, padx=5,pady=5,)

    def initWidgets_second_bottom(self):
        text_show = Text(self.fm1_bottom)
        text_show.insert(1.0,self.text_info)
        text_show.configure(state='disabled')

        text_show.pack(fill=BOTH,expand=YES, pady=5, padx=5 )

    # def set_start_event(self):
    #     self.com1.bind('<<ComboboxSelected>>', self.check_com1_state)
    #     self.com2.bind('<<ComboboxSelected>>', self.check_com2_state)
    #     # self.check_button_state()


    def check_com1_state(self,*args):
        self.lange.com1_select=self.com1.get()
        # self.select_1=self.lange.com1_select
        # print(self.lange.com1_select)
        # print(args)

    def check_com2_state(self,*args):
        self.lange.com2_select=self.com2.get()
        # self.select_2=self.lange.com1_select
        # print(self.lange.com2_select)

        # return self.lange.com2_select
        # print(self.lange.com2_select)
        # print(self.com1.set('Chinese'))
    # def check_button_state(self):
    #     if self.var_3==0:
    #
    #         self.var_3=1
    #     else:
    #         self.var_3=0


# root = Window(
#         title="易译",
#         themename="flatly",
#         size=(300, 400),
#         resizable=(True, True),
#     )
# root.attributes('-topmost',True)
#
# secondTab(root)
# root.mainloop()
