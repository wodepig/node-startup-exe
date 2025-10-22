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
import utils.file_utils as file_utils
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
    def update_progress(self, progress, downloaded, total):
        """更新进度条显示"""
        # 使用线程安全的方式更新UI
        self.ui.tk_progressbar_down_progress['value'] = progress
        label_text = (downloaded/total)*100
        self.ui.tk_label_down_label.config(text=f"已下载 {label_text:.2f} %")
    def node_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)
    def dist_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)
    def _update_btn_handle(self,evt):
        """
        处理更新按钮点击事件
        """
        self.ui.tk_button_update_btn.config(state='disabled')
        cfg = ConfigManager()
        appVersion = cfg.read("appVersion",0)
        if appVersion == 0:
            self.add_log_handle(evt, msg='初始化下载源程序...')
            if cfg.read("ulConf.fileKey",0) == 0: 
                self.add_log_handle(evt, msg='程序配置有误, 请去"关于"页面联系管理员', color='red')
                return
            downUrl = "https://api.upgrade.toolsetlink.com/v1/file/download?fileKey="+ cfg.read("ulConf.fileKey",0)
            self._start_down(downUrl,"dist.zip")
            file_utils.unzip_file('dist.zip','dist',self.add_log_handle)
            cfg.write('appVersion', 1)
            self.change_app_version_text(1)
            self.add_log_handle(evt, msg='程序初始化成功',color='green')
        else:
            self.add_log_handle(evt, msg='检查更新...')
            ak = cfg.read('ulConf.ak', '')
            sk = cfg.read('ulConf.sk', '')
            fk = cfg.read('ulConf.fileKey', '')
            client = UpgradeLinkClient(ak, sk, log_handler=self.add_log_handle)
            resp = client.get_file_upgrade(fk, version_code=appVersion)
            # print('resp.data.fileKey',resp.data.to_map()['file_key'])
            appVersion = resp.data.to_map()['versionCode']
            downPath = resp.data.to_map()['urlPath']
            if resp and resp.code == 200:
                self.add_log_handle(evt, msg=f'发现新版本:{appVersion}, 下载地址:{downPath}',color='green')
                self._start_down(downPath,"dist.zip")
                file_utils.unzip_file('dist.zip','dist',self.add_log_handle)
                cfg.write('appVersion', appVersion)
                self.change_app_version_text(appVersion)
            elif resp and  resp.code == 0:
                self.add_log_handle(evt, msg='没有新的版本',color='green')
            else:
                self.add_log_handle(evt, msg='新版本检查失败',color='red')
        self.ui.tk_button_update_btn.config(state='active')
    def change_app_version_text(self,appVersion):
        """
        改变应用版本号文本框内容
        """
        # 先取消只读状态，插入文本，再恢复只读状态
        self.ui.tk_input_app_version.config(state='normal')
        self.ui.tk_input_app_version.delete(0, 'end')  # 先清空原有内容
        self.ui.tk_input_app_version.insert(0, str(appVersion))
        self.ui.tk_input_app_version.config(state='readonly')
    def update_btn_handle(self,evt):
        if self.ui.tk_button_update_btn.state()[0] == 'disabled':
            self.add_log_handle(evt, msg='请等待任务处理完成...',color='yellow')
            return
        import threading
        download_thread = threading.Thread(
                target=self._update_btn_handle,
                args=(evt,),
                daemon=True
            )
        download_thread.start()
        # self._update_btn_handle(evt)
        # 判断是否后dist.zip文件
        # print(file_utils.get_project_root())
        # print(file_utils.check_file_exist('dist.zip'))
        # if not os.path.exists('dist.zip'):
        #     self.add_log_handle(evt, msg='请先打包dist.zip文件',color='red')
        #     return
        
        # print("检查更新处理结束:",evt)
    def start_btn_handle(self,evt):


        print("<Button-1>事件未处理:",evt)
    def _start_down(self,downUrl,fileName):
        """启动下载线程"""
        try:
            # 显示下载进度框架
            self.ui.tk_frame_down_frame.place(x=514, y=196, width=332, height=42)
            # 创建下载线程
            import threading
            download_thread = threading.Thread(
                target=file_utils.down_file,
                args=(downUrl, fileName,self.add_log_handle,self.update_progress),
                daemon=True
            )
            download_thread.start()
            download_thread.join()
            self.ui.tk_frame_down_frame.place_forget()
            # self.add_log_handle(None, f"开始下载: {fileName}")
        except Exception as e:
            self.add_log_handle(None, f"下载失败: {str(e)}", color='red')
    def stop_btn_handle(self,evt):
        file_utils.handle_node_zip(self.add_log_handle)
        print("<Button-1>事件未处理:",evt)
    def open_brower_btn_handle(self,evt):
        print("<Button-1>事件未处理:",evt)