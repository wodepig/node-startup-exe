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
        self.tk_tabs_mgukgrl3 = self.__tk_tabs_mgukgrl3(self)
        self.tk_select_box_update_type = self.__tk_select_box_update_type( self.tk_tabs_mgukgrl3_1)
        self.tk_label_mgyhc1dz = self.__tk_label_mgyhc1dz( self.tk_tabs_mgukgrl3_1)
        self.tk_button_check_conf_btn = self.__tk_button_check_conf_btn( self.tk_tabs_mgukgrl3_1)
        self.tk_button_save_conf_btn = self.__tk_button_save_conf_btn( self.tk_tabs_mgukgrl3_1)
        self.tk_frame_ul_confg_dialog = self.__tk_frame_ul_confg_dialog( self.tk_tabs_mgukgrl3_1)
        self.tk_input_ul_sk = self.__tk_input_ul_sk( self.tk_frame_ul_confg_dialog) 
        self.tk_label_mgyhdswe = self.__tk_label_mgyhdswe( self.tk_frame_ul_confg_dialog) 
        self.tk_label_mgyhdbgc = self.__tk_label_mgyhdbgc( self.tk_frame_ul_confg_dialog) 
        self.tk_input_ul_url = self.__tk_input_ul_url( self.tk_frame_ul_confg_dialog) 
        self.tk_label_open_url = self.__tk_label_open_url( self.tk_frame_ul_confg_dialog) 
        self.tk_input_ul_filekey = self.__tk_input_ul_filekey( self.tk_frame_ul_confg_dialog) 
        self.tk_input_ul_ak = self.__tk_input_ul_ak( self.tk_frame_ul_confg_dialog) 
        self.tk_label_mgyhdxym = self.__tk_label_mgyhdxym( self.tk_frame_ul_confg_dialog) 
        self.tk_frame_fix_config_dialog = self.__tk_frame_fix_config_dialog( self.tk_tabs_mgukgrl3_1)
        self.tk_label_mgyibdn0 = self.__tk_label_mgyibdn0( self.tk_frame_fix_config_dialog) 
        self.tk_input_down_url = self.__tk_input_down_url( self.tk_frame_fix_config_dialog) 
        self.tk_frame_url_config_dialog = self.__tk_frame_url_config_dialog( self.tk_tabs_mgukgrl3_1)
        self.tk_label_mgyij1po = self.__tk_label_mgyij1po( self.tk_frame_url_config_dialog) 
        self.tk_input_url_url = self.__tk_input_url_url( self.tk_frame_url_config_dialog) 
        self.tk_frame_mgyh9kz6 = self.__tk_frame_mgyh9kz6(self)
        self.tk_text_main_log = self.__tk_text_main_log( self.tk_frame_mgyh9kz6) 
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 849
        height = 640
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
    def __tk_tabs_mgukgrl3(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_mgukgrl3_0 = self.__tk_frame_mgukgrl3_0(frame)
        frame.add(self.tk_tabs_mgukgrl3_0, text="开始")
        self.tk_tabs_mgukgrl3_1 = self.__tk_frame_mgukgrl3_1(frame)
        frame.add(self.tk_tabs_mgukgrl3_1, text="设置")
        frame.place(x=1, y=0, width=848, height=267)
        return frame
    def __tk_frame_mgukgrl3_0(self,parent):
        frame = Frame(parent)
        frame.place(x=1, y=0, width=848, height=267)
        return frame
    def __tk_frame_mgukgrl3_1(self,parent):
        frame = Frame(parent)
        frame.place(x=1, y=0, width=848, height=267)
        return frame
    def __tk_select_box_update_type(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("UpgradeLin","固定链接","固定url")
        cb.place(x=98, y=15, width=150, height=30)
        return cb
    def __tk_label_mgyhc1dz(self,parent):
        label = Label(parent,text="更新方式",anchor="center", )
        label.place(x=25, y=16, width=50, height=30)
        return label
    def __tk_button_check_conf_btn(self,parent):
        btn = Button(parent, text="检查", takefocus=False,)
        btn.place(x=669, y=156, width=50, height=30)
        return btn
    def __tk_button_save_conf_btn(self,parent):
        btn = Button(parent, text="保存", takefocus=False,)
        btn.place(x=745, y=156, width=50, height=30)
        return btn
    def __tk_frame_ul_confg_dialog(self,parent):
        frame = Frame(parent,)
        frame.place(x=19, y=65, width=819, height=90)
        return frame
    def __tk_input_ul_sk(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=306, y=0, width=180, height=30)
        return ipt
    def __tk_label_mgyhdswe(self,parent):
        label = Label(parent,text="AK",anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label
    def __tk_label_mgyhdbgc(self,parent):
        label = Label(parent,text="唯一ID",anchor="center", )
        label.place(x=570, y=0, width=50, height=30)
        return label
    def __tk_input_ul_url(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=51, y=60, width=180, height=30)
        return ipt
    def __tk_label_open_url(self,parent):
        label = Label(parent,text="url",anchor="center", )
        label.place(x=0, y=60, width=50, height=30)
        return label
    def __tk_input_ul_filekey(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=622, y=0, width=180, height=30)
        return ipt
    def __tk_input_ul_ak(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=46, y=0, width=180, height=30)
        return ipt
    def __tk_label_mgyhdxym(self,parent):
        label = Label(parent,text="SK",anchor="center", )
        label.place(x=255, y=0, width=50, height=30)
        return label
    def __tk_frame_fix_config_dialog(self,parent):
        frame = Frame(parent,)
        frame.place(x=19, y=65, width=819, height=90)
        return frame
    def __tk_label_mgyibdn0(self,parent):
        label = Label(parent,text="下载地址",anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label
    def __tk_input_down_url(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=79, y=0, width=180, height=30)
        return ipt
    def __tk_frame_url_config_dialog(self,parent):
        frame = Frame(parent,)
        frame.place(x=19, y=65, width=819, height=90)
        return frame
    def __tk_label_mgyij1po(self,parent):
        label = Label(parent,text="网址",anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label
    def __tk_input_url_url(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=77, y=0, width=180, height=30)
        return ipt
    def __tk_frame_mgyh9kz6(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=266, width=848, height=373)
        return frame
    def __tk_text_main_log(self,parent):
        text = Text(parent)
        text.place(x=0, y=0, width=846, height=373)
        self.create_bar(parent, text,True, False, 0, 0, 846,373,848,373)
        return text
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_select_box_update_type.bind('<<ComboboxSelected>>',self.ctl.change_update_type)
        self.tk_button_check_conf_btn.bind('<Button-1>',self.ctl.check_conf_btn_handle)
        self.tk_button_save_conf_btn.bind('<Button-1>',self.ctl.save_conf_btn_handle)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()