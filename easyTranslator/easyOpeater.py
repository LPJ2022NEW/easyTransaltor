import pyperclip
from pynput.mouse import Listener
import pyautogui as auto
import keyboard
import threading
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