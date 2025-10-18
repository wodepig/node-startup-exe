"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_mgvyhx7m = self.__tk_tabs_mgvyhx7m(self)
        self.tk_label_mgvyirxi = self.__tk_label_mgvyirxi( self.tk_tabs_mgvyhx7m_1)
        self.tk_label_mgvyj0z2 = self.__tk_label_mgvyj0z2( self.tk_tabs_mgvyhx7m_0)
        self.tk_button_add_log = self.__tk_button_add_log( self.tk_tabs_mgvyhx7m_0)
        self.tk_frame_mgvyqw0h = self.__tk_frame_mgvyqw0h(self)
        self.tk_text_main_log = self.__tk_text_main_log( self.tk_frame_mgvyqw0h) 
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 681
        height = 448
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_tabs_mgvyhx7m(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_mgvyhx7m_0 = self.__tk_frame_mgvyhx7m_0(frame)
        frame.add(self.tk_tabs_mgvyhx7m_0, text="主页")
        self.tk_tabs_mgvyhx7m_1 = self.__tk_frame_mgvyhx7m_1(frame)
        frame.add(self.tk_tabs_mgvyhx7m_1, text="日志")
        frame.place(x=0, y=0, width=681, height=187)
        return frame
    def __tk_frame_mgvyhx7m_0(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=681, height=187)
        return frame
    def __tk_frame_mgvyhx7m_1(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=681, height=187)
        return frame
    def __tk_label_mgvyirxi(self,parent):
        label = Label(parent,text="我是日志",anchor="center", )
        label.place(x=260, y=80, width=50, height=30)
        return label
    def __tk_label_mgvyj0z2(self,parent):
        label = Label(parent,text="我是主页",anchor="center", )
        label.place(x=32, y=28, width=50, height=30)
        return label
    def __tk_button_add_log(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=160, y=30, width=50, height=30)
        return btn
    def __tk_frame_mgvyqw0h(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=197, width=681, height=251)
        return frame
    def __tk_text_main_log(self,parent):
        text = Text(parent)
        text.place(x=0, y=0, width=679, height=251)
        self.create_bar(parent, text,True, False, 0, 0, 679,251,681,251)
        return text
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_add_log.bind('<Button-1>',self.ctl.add_log_handle)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()