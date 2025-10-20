import datetime

def get_current_hms():
    """
    获取当前时间的时分秒
    
    返回:
        str: 格式为 HH:MM:SS 的时间字符串
    """
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")
