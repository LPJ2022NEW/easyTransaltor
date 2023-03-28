import pyautogui
#pyinstaller -F -w --clean --exclude matplotlib -p C:\Anaconda2\envs\paddleocr\Lib\shite-packages\paddleocr;C:\Anaconda2\envs\paddleocr\Lib\site-packages\paddle\libs scr2txt.py -i scr2txt.ico --add-binary C:\Anaconda2\envs\paddleocr\Lib\site-packages\paddle\libs;. --add-data C:\opencode\ocr\scr2txt\model;.\model --add-data C:\opencode\ocr\scr2txt\model\scr2txt.ico;.\ --additional-hooks-dir=.
from firstPage import firstTab
from Second_Page import secondTab
from sangPage3 import songPageEvent
from ttkbootstrap import *


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