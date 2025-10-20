"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from ui import Win  
from utils import get_current_hms
from upgrade_link_utils import format_upgrade_link
# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def add_log_handle(self,evt,msg):
        """
        处理日志输出
        """
        self.ui.tk_text_main_log.insert("end",f"{get_current_hms()} {msg}\n")
        # 自动滚动到文本框底部
        self.ui.tk_text_main_log.see("end")
    def log_handler(msg):
        self.add_log_handle(evt, msg)
    def change_update_type(self,evt):
        """
        处理升级类型选择框选择事件
        """
        if evt.widget.get() == 'UpgradeLin':
            self.ui.tk_frame_ul_confg_dialog.place(x=19, y=65, width=819, height=90)
            self.ui.tk_frame_fix_config_dialog.place_forget()
            self.ui.tk_frame_url_config_dialog.place_forget()
        elif evt.widget.get() == '固定链接':
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place(x=19, y=65, width=819, height=90)
            self.ui.tk_frame_url_config_dialog.place_forget()
        elif evt.widget.get() == '固定url':
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place_forget()
            self.ui.tk_frame_url_config_dialog.place(x=19, y=65, width=819, height=90)
        else:
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place_forget()
            self.ui.tk_frame_url_config_dialog.place_forget()
    def check_conf_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)
    def save_conf_btn_handle(self,evt):
        """
        处理保存配置按钮点击事件
        """
        format_upgrade_link('888', self.add_log_handle(evt, msg='888'))
        self.ui.tk_ak
        print("<Button-1>事件未处理:",evt)
