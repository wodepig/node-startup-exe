# http://upgrade.toolsetlink.com/的工具类
def check_config(ak, sk, fk, log_handler=None):
    """
    检查配置是否完整
    Args:
        ak: 访问密钥
        sk: 密钥
        fk: 文件id
        log_handler: 可选的日志处理函数，接收消息作为参数
    """
    if not all([ak, sk, fk]):
        if log_handler:
            log_handler(evt=None,msg="配置不完整，缺少访问密钥、密钥或fileKey", color='red')
        return False
    return True
    # 发请求测试
    

def format_upgrade_link(link, log_handler=None):
    """
    格式化升级链接，添加换行符
    
    Args:
        link: 需要格式化的链接字符串
        log_handler: 可选的日志处理函数，接收消息作为参数
    """
    try:
        result = link.replace("\\n", "\n")
        if log_handler:
            log_handler(msg=f"成功格式化升级链接: {link}", color='green')
        return result
    except Exception as e:
        if log_handler:
            log_handler(msg=f"格式化升级链接时出错: {str(e)}", color='red')
        raise
