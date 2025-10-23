"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from ast import For
from ui import Win  
import time
import subprocess
import sys
from pathlib import Path
import utils.file_utils as file_utils
from utils.utils import get_port_from_url,get_current_hms,get_system_architecture,get_system_login_user
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
        # 状态变量
        self.node_process = None
        # TODO 组件初始化 赋值操作
    def initConfig(self):
        cfg = ConfigManager()
        # 初始化更新类型
        updateType = cfg.read('updateType','UpgradeLin')
        updateTypeList = ['UpgradeLin','下载更新','打开网页']
        self.ui.tk_select_box_update_type.current(updateTypeList.index(updateType))
        self.change_update_type(None)
        # 初始化值
        ulConf = cfg.read('ulConf',{})
        self.ui.tk_input_ul_ak.insert(0,ulConf.get('ak',''))
        self.ui.tk_input_ul_sk.insert(0,ulConf.get('sk',''))
        if  ulConf.get('url','') == '':
            self.ui.tk_input_ul_url.insert(0,"http://localhost:3000")
        else:
            self.ui.tk_input_ul_url.insert(0,ulConf.get('url',''))
        self.ui.tk_input_ul_filekey.insert(0,ulConf.get('fileKey',''))
        # 下载更新的配置
        downConf = cfg.read('downConf',{})
        if downConf.get('url','') == '':
            self.ui.tk_input_down_url.insert(0,"http://localhost:3000")
        else:
            self.ui.tk_input_down_url.insert(0,downConf.get('url',''))
        self.ui.tk_input_down_open_url.insert(0,downConf.get('openUrl',''))
        updateTimeType = downConf.get('updateTime','每次启动时')
        updateTimeTypeList = ['每次启动时','从不']
        self.ui.tk_select_box_down_update_time.current(updateTimeTypeList.index(updateTimeType))
        # 打开网页的配置
        openConf = cfg.read('openConf',{})
        if openConf.get('url','') == '':
            self.ui.tk_input_url_url.insert(0,"http://localhost:3000")
        else:
            self.ui.tk_input_url_url.insert(0,openConf.get('url',''))
        self.add_log_handle(None, "更新配置加载完成...")
        # 加载系统信息
        self.ui.tk_input_sys_version.insert(0,get_system_architecture())
        self.ui.tk_input_sys_version.config(state='readonly')
        self.ui.tk_input_sys_user.insert(0,get_system_login_user())
        self.ui.tk_input_sys_user.config(state='readonly')
        self.ui.tk_input_app_version.insert(0,cfg.read('appVersion',''))
        self.ui.tk_input_app_version.config(state='readonly')
        self.add_log_handle(None, "系统信息加载完成...")
        # 加载作者信息
        self.ui.tk_input_author_email.insert(0,cfg.read('author.email','作者邮箱'))
        self.ui.tk_input_author_email.config(state='readonly')
        self.ui.tk_input_author_wx.insert(0,cfg.read('author.wx','作者微信'))
        self.ui.tk_input_author_wx.config(state='readonly')
        self.ui.tk_input_author_web.insert(0,cfg.read('author.url','作者个人网站'))
        self.ui.tk_input_author_web.config(state='readonly')
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
            # 设置默认值
        elif type == '下载更新':
            self.ui.tk_frame_ul_confg_dialog.place_forget()
            self.ui.tk_frame_fix_config_dialog.place(x=19, y=65, width=819, height=90)
            self.ui.tk_frame_url_config_dialog.place_forget()
        elif type == '打开网页':
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
                return True
            else:
                self.add_log_handle(evt, msg='配置检查失败',color='red')
                return False
        elif updateType == '下载更新':
            downUrl = self.ui.tk_input_down_url.get()
            openUrl = self.ui.tk_input_down_open_url.get()
            downType = self.ui.tk_select_box_down_update_time.get()
            if not downUrl or not openUrl or not downType:
                self.add_log_handle(evt, msg='请填写完整下载配置',color='red')
                return False
            self.add_log_handle(evt, msg='配置检查成功',color='green')
        elif updateType == '打开网页':
            openUrl = self.ui.tk_input_url_url.get()
            if not openUrl:
                self.add_log_handle(evt, msg='请填写完整',color='red')
                return False
            self.add_log_handle(evt, msg='配置检查成功',color='green')
        else:
            self.add_log_handle(evt, msg='暂未实现',color='yellow')
            return False
        return True
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
                cfg.write('appConfig.url', openUrl)
                cfg.write('appConfig.port', get_port_from_url(openUrl))
                self.add_log_handle(evt, msg='配置保存成功',color='green')
            else:
                self.add_log_handle(evt, msg='配置保存失败',color='red')
        elif updateType == '下载更新':
            downUrl = self.ui.tk_input_down_url.get()
            openUrl = self.ui.tk_input_down_open_url.get()
            downType = self.ui.tk_select_box_down_update_time.get()
            if not downUrl or not openUrl or not downType:
                self.add_log_handle(evt, msg='请填写完整下载配置',color='red')
                return False
            # 保存配置
            cfg = ConfigManager()
            cfg.write('downConf.url', downUrl)
            cfg.write('downConf.openUrl', openUrl)
            cfg.write('downConf.updateTime', downType)
            cfg.write('updateType', '下载更新')
            cfg.write('appConfig.url', openUrl)
            cfg.write('appConfig.port', get_port_from_url(openUrl))
            self.add_log_handle(evt, msg='配置保存成功',color='green')
        elif updateType == '打开网页':
            openUrl = self.ui.tk_input_url_url.get()
            if not openUrl:
                self.add_log_handle(evt, msg='请填写完整',color='red')
                return False
            # 保存配置
            cfg = ConfigManager()
            cfg.write('openConf.url', openUrl)
            cfg.write('updateType', '打开网页')
            cfg.write('appConfig.url', openUrl)
            cfg.write('appConfig.port', get_port_from_url(openUrl))
            self.add_log_handle(evt, msg='配置保存成功',color='green')
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
        if cfg.read("updateType",'') == '打开网页':
            self.add_log_handle(evt, msg='无需更新源码, 跳过', color='yellow')
            self.ui.tk_button_update_btn.config(state='active')
            return
        appVersion = cfg.read("appVersion",0)
        if appVersion == 0 or not file_utils.check_file_exist('dist'):
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
        # 检查更新
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
    def _handle_node_zip(self,evt):
        cfg = ConfigManager()
        if cfg.read("updateType",'') == '打开网页':
            self.add_log_handle(evt, msg='无需检查Node, 跳过', color='yellow')
            return
        if  file_utils.check_file_exist('node'):
            self.add_log_handle(None,msg="node目录已存在，无需处理",color="green")
            return True
        if  file_utils.check_file_exist('node.zip'):
            self.add_log_handle(None,msg="node.zip文件已存在，直接解压")
            if not file_utils.handle_node_zip(self.add_log_handle):
                return False
            return True
        sysVersion = get_system_architecture()
        cfg = ConfigManager()
        nodeDownUrl = cfg.read(f'nodeVersion.{sysVersion}','')
        if nodeDownUrl == '':
            self.add_log_handle(evt, msg=f'未配置{sysVersion}的node下载地址',color='red')
            return False
        self._start_down(nodeDownUrl,"node.zip")
        if not file_utils.handle_node_zip(self.add_log_handle):
            return False
        return True

    def read_process_output_thread(self):
        """在单独线程中读取进程输出"""
        while self.node_process is not None and self.node_process.poll() is None:
            try:
                output = self.node_process.stdout.readline()
                if output:
                    # 使用线程安全的方式更新UI
                    self.ui.after(0, lambda: self.add_log_handle(None,'程序输出:' + output.strip()))
            except Exception as e:
                if "I/O operation on closed file" not in str(e):
                    self.ui.after(0, lambda: self.add_log_handle(None,f"读取输出时出错: {str(e)}",color="red"))
                break
    
    def reset_btn(self):
        self.ui.tk_button_start_btn.config(state='active')
        self.ui.tk_button_stop_btn.config(state='active')
        self.ui.tk_button_update_btn.config(state='active')
    def _start_btn_handle(self,evt):
        """启动程序"""
        cfg = ConfigManager()
        if cfg.read("updateType",'') == '打开网页':
            self.add_log_handle(evt, msg='无需启动程序, 跳过', color='yellow')
            return True
        self.reset_btn()
        self.ui.tk_button_start_btn.config(state='disabled')
        self.ui.tk_button_update_btn.config(state='disabled')
        if self.node_process is not None and self.node_process.poll() is None:
            self.add_log_handle(None,msg="服务已经在运行中",color="yellow")
            self.reset_btn()
            return False
        if not file_utils.check_file_exist('dist','server','index.mjs'):
            self.add_log_handle(None,msg="源程序不存在，无法启动程序",color="red")
            self.reset_btn()
            return False
        if not file_utils.check_file_exist('node','node.exe'):
            self.add_log_handle(None,msg="启动器不存在，无法启动程序",color="red")
            self.reset_btn()
            return False
        node_process = file_utils.start_node_server(self.add_log_handle)
        if not node_process:
            self.reset_btn()
            return False
        self.node_process = node_process
        # 读取输出
        import threading
        node_thread = threading.Thread(
                target=self.read_process_output_thread,
                daemon=True
            )
        node_thread.start()
        # self.read_process_output_thread()
        # self.add_log_handle(None, f"开始启动程序...", color='green')
        # self.add_log_handle(None, f"程序启动成功", color='green')
        self.ui.tk_button_start_btn.config(state='disabled')
        self.ui.tk_button_stop_btn.config(state='active')
        self.ui.tk_button_update_btn.config(state='disabled')
        return True
    def start_btn_handle(self,evt):
        if self.ui.tk_button_start_btn.state()[0] == 'disabled':
            self.add_log_handle(evt, msg='请等待任务处理完成...',color='yellow')
            return
        import threading
        download_thread = threading.Thread(
                target=self._start_btn_handle,
                args=(evt,),
                daemon=True
            )
        download_thread.start()
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
    def _stop_btn_handle(self,evt):
        """停止Node服务"""
        if self.node_process is None or self.node_process.poll() is not None:
            self.add_log_handle(None,msg="服务没有在运行",color="yellow")
            self.reset_btn()
            return    
        try:
            self.add_log_handle(None,msg="正在停止服务...",color="yellow")
            self.node_process.terminate()
            # 等待进程结束
            timeout = 10
            start_time = time.time()
            while self.node_process.poll() is None and time.time() - start_time < timeout:
                time.sleep(0.5)
                
            if self.node_process.poll() is None:
                # 强制终止
                self.node_process.kill()
                
            self.add_log_handle(None,msg="服务已停止")

        except Exception as e:
            self.add_log_handle(None,msg=f"停止服务时出错: {str(e)}",color="red")
        finally:
            self.node_process = None
             # 重置按钮状态
            self.reset_btn()
    def open_browser_btn_handle(self,evt):
        """打开浏览器访问服务"""
        cfg = ConfigManager()
        url = cfg.read("appConfig.url","")
        if not url:
            self.add_log_handle(None,msg="未配置启动URL，无法打开浏览器",color="yellow")
            return
        if cfg.read("updateType","UpgradeLin") != "打开网页":
            if self.node_process is None or self.node_process.poll() is not None:
                self.add_log_handle(None,msg="服务未运行，无法打开浏览器",color="yellow")
                return
        self.add_log_handle(None,msg=f"打开浏览器访问: {url}",color="green")
        import webbrowser
        webbrowser.open(url)
    def handle_node_btn_click(self,evt):
        """处理Node.zip文件"""
        import threading
        handle_thread = threading.Thread(
                target=self._handle_node_zip,
                args=(evt,),
                daemon=True
            )
        handle_thread.start()
    def clear_btn_handle(self,evt):
        """清除node目录"""
        file_utils.remove_item('node','node_tmp','dist','node.zip','dist.zip')
        self.add_log_handle(None,msg="相关目录已清除", color='green')
    def stop_btn_handle(self,evt):
        if self.ui.tk_button_stop_btn.state()[0] == 'disabled':
            self.add_log_handle(evt, msg='请等待任务处理完成...',color='yellow')
            return
        import threading
        download_thread = threading.Thread(
                target=self._stop_btn_handle,
                args=(evt,),
                daemon=True
            )
        download_thread.start()
    def one_start_btn_click(self, evt):
        # 一键启动服务：先更新再切换按钮显示
        if self.ui.tk_button_one_start_btn.state()[0] == 'disabled':
            self.add_log_handle(evt, msg='请等待任务处理完成...',color='yellow')
            return
        def _run():
            try:
                self._update_btn_handle(evt)
                self._handle_node_zip(evt)
                if self._start_btn_handle(evt):
                    self.open_browser_btn_handle(evt)
            except Exception as e:
                self.add_log_handle(None,msg=f"一键启动服务时出错: {str(e)}",color="red")
            finally:
                self.ui.tk_button_one_start_btn.config(state='active')
        self.ui.tk_button_one_start_btn.config(state='disabled')
        import threading
        start_thread = threading.Thread(target=_run, daemon=True)
        start_thread.start()
    def admin_check_change(self,evt):
        type = self.ui.admin_check_var.get()
        if type:
            # self.add_log_handle(None,msg="展示普通按钮")
            self.ui.tk_frame_normal_btns.place(x=454, y=0, width=394, height=148)
            self.ui.tk_frame_admin_btns.place_forget()
        else:
            # self.add_log_handle(None,msg="展示高级按钮")
            self.ui.tk_frame_normal_btns.place_forget()
            self.ui.tk_frame_admin_btns.place(x=454, y=0, width=394, height=148)
    def close_handle(self,evt):
        """处理窗口销毁事件，防止多次调用"""
        # 检查是否是主窗口的销毁事件（不是子控件的）
        if evt.widget == self.ui:
            # 使用标志位防止多次调用
            if not hasattr(self, '_destroy_called'):
                self._destroy_called = True
                print("应用程序正在关闭...")
                
                # 停止正在运行的Node服务
                if hasattr(self, 'node_process') and self.node_process is not None:
                    try:
                        if self.node_process.poll() is None:
                            self.node_process.terminate()
                            # 等待进程结束
                            import time
                            timeout = 5
                            start_time = time.time()
                            while self.node_process.poll() is None and time.time() - start_time < timeout:
                                time.sleep(0.1)
                            
                            if self.node_process.poll() is None:
                                self.node_process.kill()
                    except Exception as e:
                        print(f"停止服务时出错: {e}")
                
                # 清理资源 - 使用print而不是add_log_handle，因为UI可能已经销毁
                print("应用程序关闭完成")