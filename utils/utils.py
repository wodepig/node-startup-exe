import datetime
import platform
import os

def get_current_hms():
    """
    获取当前时间的时分秒
    
    返回:
        str: 格式为 HH:MM:SS 的时间字符串
    """
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")



def get_system_login_user():
    """
    获取系统的登陆用户名，不报错
    
    返回:
        str: 系统登陆用户名，如果获取失败则返回空字符串
    """
    try:
        return os.getlogin()
    except Exception:
        return ''

def get_system_architecture():
    """
    获取系统的架构信息
    返回:
        str: 格式如 win_64, win_32 这样的系统架构字符串
    """
    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == 'windows':
        if '64' in machine:
            return 'win_64'
        else:
            return 'win_32'
    # 可根据需要扩展其他系统的架构返回值
    return f"{system}_{machine}"
