"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from ui import Win  
from utils import get_current_hms
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
    def add_log_handle(self,evt):
        """
        处理日志输出
        """
        self.ui.tk_text_main_log.insert("end",f"{get_current_hms()} <Button-1>事件未处理:{evt}\n")
        print("<Button-1>事件未处理:",evt)
        # 自动滚动到文本框底部
        self.ui.tk_text_main_log.see("end")
