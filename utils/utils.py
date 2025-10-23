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
        str: 格式如 win7_32,win11_64 这样的系统架构字符串
    """
    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == 'windows':
        # 获取 Windows 版本号
        version = platform.version()
        try:
            major, _ = map(int, version.split('.')[:2])
            # 根据版本号映射到常见 Windows 名称
            if major == 10:
                # Windows 10 和 11 共用 10.0，通过 build 号区分
                build = int(version.split('.')[2]) if len(version.split('.')) > 2 else 0
                win_name = 'win11' if build >= 22000 else 'win10'
            elif major == 6:
                if _ == 3:
                    win_name = 'win81'
                elif _ == 2:
                    win_name = 'win8'
                elif _ == 1:
                    win_name = 'win7'
                else:
                    win_name = 'winvista'
            elif major == 5:
                win_name = 'winxp'
            else:
                win_name = 'win'
        except Exception:
            win_name = 'win'
        arch = '64' if '64' in machine else '32'
        return f"{win_name}_{arch}"
    # 可根据需要扩展其他系统的架构返回值
    return f"{system}_{machine}"
# print(get_system_architecture())