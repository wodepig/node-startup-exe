"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from ast import For
from ui import Win  
import time
import sys
from pathlib import Path
from utils.file_utils import get_project_root,check_file_exist,down_file
from utils.utils import get_current_hms,get_system_architecture,get_system_login_user
from utils.upgrade_link_utils import check_config, format_upgrade_link,get_new_version
from utils.upgrade_utils import UpgradeLinkClient
from ConfigManager import ConfigManager

# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):
        self.current_dir = Path(sys.argv[0]).parent.resolve()
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        self.initConfig()
        # 隐藏下载信息
        self.ui.tk_frame_down_frame.place_forget()
        # TODO 组件初始化 赋值操作
    def initConfig(self):
        cfg = ConfigManager()
        # 初始化更新类型
        updateType = cfg.read('updateType','UpgradeLin')
        updateTypeList = ['UpgradeLin','固定链接','固定url']
        self.ui.tk_select_box_update_type.current(updateTypeList.index(updateType))
        self.change_update_type(None)
        # 初始化值
        ulConf = cfg.read('ulConf',{})
        self.ui.tk_input_ul_ak.insert(0,ulConf.get('ak',''))
        self.ui.tk_input_ul_sk.insert(0,ulConf.get('sk',''))
        self.ui.tk_input_ul_url.insert(0,ulConf.get('url',''))
        self.ui.tk_input_ul_filekey.insert(0,ulConf.get('fileKey',''))
        self.add_log_handle(None, "更新配置加载完成...")
        # 加载系统信息
        self.ui.tk_input_sys_version.insert(0,get_system_architecture())
        self.ui.tk_input_sys_version.config(state='readonly')
        self.ui.tk_input_sys_user.insert(0,get_system_login_user())
        self.ui.tk_input_sys_user.config(state='readonly')
        self.ui.tk_input_app_version.insert(0,cfg.read('appVersion',''))
        self.ui.tk_input_app_version.config(state='readonly')
        self.add_log_handle(None, "系统信息加载完成...")
    def add_log_handle(self, evt, msg, color='black'):
        """
        处理日志输出
        """
        # 为文本框添加标签配置，设置文字颜色
        bg_color = 'black' if color == 'yellow' else 'white'
        self.ui.tk_text_main_log.tag_configure(color, foreground=color, background=bg_color)
        self.ui.tk_text_main_log.insert("end", f"{get_current_hms()} {msg}\n", color)
        # 自动滚动到文本框底部
        self.ui.tk_text_main_log.see("end")
    def log_handler(msg):
        self.add_log_handle(evt, msg)
    def change_update_type(self,evt):
        """
        处理升级类型选择框选择事件
        """
        type = ''
        if not evt:
            type = self.ui.tk_select_box_update_type.get()
        else:
            type = evt.widget.get()
        if type == 'UpgradeLin':
            self.ui.tk_frame_ul_confg_dialog.place(x=19, y=65, width=819, height=90)
            self.ui.tk_frame_fix_config_dialog.place_forget()
            self.ui.tk_frame_url_config_dialog.place_forget()
        elif type == '固定链接':
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place(x=19, y=65, width=819, height=90)
            self.ui.tk_frame_url_config_dialog.place_forget()
        elif type == '固定url':
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place_forget()
            self.ui.tk_frame_url_config_dialog.place(x=19, y=65, width=819, height=90)
        else:
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place_forget()
            self.ui.tk_frame_url_config_dialog.place_forget()
    def check_conf_btn_handle(self,evt):
        """
        处理检查配置按钮点击事件
        """
        updateType = self.ui.tk_select_box_update_type.get()
        if updateType == 'UpgradeLin':
            ak = self.ui.tk_input_ul_ak.get()
            sk = self.ui.tk_input_ul_sk.get()
            fk = self.ui.tk_input_ul_filekey.get()
            client = UpgradeLinkClient(ak, sk, log_handler=self.add_log_handle)
            resp = client.get_file_upgrade(fk)
            if resp and (resp.code == 200 or resp.code == 0):
                self.add_log_handle(evt, msg='配置检查成功',color='green')
            else:
                self.add_log_handle(evt, msg='配置检查失败',color='red')
        elif updateType == '固定链接':
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
        elif updateType == '固定url':
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
        else:
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
    def save_conf_btn_handle(self,evt):
        """
        处理保存配置按钮点击事件
        """
        updateType = self.ui.tk_select_box_update_type.get()
        if updateType == 'UpgradeLin':
            ak = self.ui.tk_input_ul_ak.get()
            sk = self.ui.tk_input_ul_sk.get()
            fk = self.ui.tk_input_ul_filekey.get()
            openUrl = self.ui.tk_input_ul_url.get()
            client = UpgradeLinkClient(ak, sk, log_handler=self.add_log_handle)
            resp = client.get_file_upgrade(fk)
            if resp and (resp.code == 200 or resp.code == 0):
                # 保存配置
                cfg = ConfigManager()
                cfg.write('ulConf.ak', ak)
                cfg.write('ulConf.ak', ak)
                cfg.write('ulConf.sk', sk)
                cfg.write('ulConf.fileKey', fk)
                cfg.write('updateType', 'UpgradeLin')
                self.add_log_handle(evt, msg='配置保存成功',color='green')
            else:
                self.add_log_handle(evt, msg='配置保存失败',color='red')
        elif updateType == '固定链接':
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
        elif updateType == '固定url':
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
        else:
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
    def node_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)
    def dist_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)
    def update_btn_handle(self,evt):
        self.ui.tk_button_update_btn.config(state='disabled')
        cfg = ConfigManager()
        appVersion = cfg.read("appVersion",0)
        if appVersion == 0:
            self.add_log_handle(evt, msg='初始化下载源程序...')
            downUrl = "https://api.upgrade.toolsetlink.com/v1/file/download?fileKey="+ cfg.read("ulConf.fileKey",0)
            down_file(downUrl,'dist.zip')
        else:
            self.add_log_handle(evt, msg='检查更新...')
        # 判断是否后dist.zip文件
        print(get_project_root())
        print(check_file_exist('dist.zip'))
        # if not os.path.exists('dist.zip'):
        #     self.add_log_handle(evt, msg='请先打包dist.zip文件',color='red')
        #     return
        print("<Button-1>事件未处理:",evt)
    def start_btn_handle(self,evt):
        self.ui.tk_frame_down_frame.place(x=514, y=196, width=332, height=42)
        time.sleep(1)
        for i in range(20):
            print(f"倒计时 {20-i} 秒")
            self.ui.tk_progressbar_down_progress['value'] = i*5
            self.ui.tk_label_down_label.config(text=f"倒计时 {20-i} 秒")
            time.sleep(1)
        print("20秒倒计时结束")
        print("<Button-1>事件未处理:",evt)
    def stop_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)
    def open_brower_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)